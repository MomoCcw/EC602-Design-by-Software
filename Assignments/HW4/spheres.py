#!/usr/bin/env python
# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# Copyright 2021 Zhaozhong Qi zqi5@bu.edu

import numpy as np
import math
import sys

class Sphere:
    def __init__(self, mass, radius, p_x, p_y, p_z, v_x, v_y, v_z, name):
        self.mass = mass
        self.radius = radius
        self.name = name
        self.velocity = np.array([v_x, v_y, v_z])
        self.position = np.array([p_x, p_y, p_z])

def energy(sphere_list):
    accum = 0
    for i in sphere_list:
        accum += 0.5*i.mass*(np.linalg.norm(i.velocity)**2)
    return round(accum,2)

def momentum(sphere_list):
    accum = np.array([0,0,0])
    for i in sphere_list:
        accum = accum + (i.velocity*i.mass)
    return np.round(accum,decimals=2)

def quadratic_solve(a:float,b:float,c:float) -> float:
    d = (b**2) - (4*a*c)
    if d < 0:
        return None
    r1 = float(-b+math.sqrt(d))/(2*a)
    r2 = float(-b-math.sqrt(d))/(2*a)
    ans = []
    if r1 >= 0:
        ans.append(r1)
    if r2 >= 0:
        ans.append(r2)
    return round(min(ans),4)

class World:
    def __init__(self, radius, duration, sphere):
        self.radius = radius
        self.duration = duration
        self.sphere_list = sphere
        self.velocity = np.array([0, 0, 0])
        self.position = np.array([0, 0, 0])
        self.time_track = [0]
        self.current_time_track = [0]
        self.all_accident = {}

    def collision(self, one, two) -> bool:
        if ((two.position - one.position).dot(two.velocity - one.velocity)) < 0:
            return True
        else:
            return False

    def static(self, one) -> bool:
        velocity_1 = one.velocity
        if (velocity_1[0] == 0) & (velocity_1[1] == 0) & (velocity_1[2] == 0):
            return True
        else:
            return False

    def collide_time(self,one,two):
        p_new = two.position - one.position
        v_new = two.velocity - one.velocity
        radius_sum = one.radius + two.radius
        #  a*t^2 + b*t + c = 0
        a = np.linalg.norm(v_new)**2
        b = 2*p_new.dot(v_new)
        c = np.linalg.norm(p_new)**2 - radius_sum**2
        return quadratic_solve(a,b,c)

    def reflect_time(self,one):
        p_new = one.position - self.position
        v_new = one.velocity - self.velocity
        radius_diff = self.radius - one.radius
        #  a*t^2 + b*t + c = 0
        a = np.linalg.norm(v_new)**2
        b = 2*p_new.dot(v_new)
        c = np.linalg.norm(p_new)**2 - radius_diff**2
        return quadratic_solve(a,b,c)

    def collision_update(self, one,two) -> list:
        "Return each ball's new position and new velocity after collision"
        "[new_p_one, new_p_two, new_v_one, new_v_two]"

        time_diff = self.collide_time(one,two)
        new_p_one = one.position + one.velocity*time_diff
        new_p_two = two.position + two.velocity*time_diff

        new_v_one = one.velocity-(2*two.mass/(one.mass+two.mass))\
        *(((one.velocity-two.velocity).dot(one.position-two.position))/\
            ((one.position-two.position).dot(one.position-two.position)))\
        *(one.position-two.position)

        new_v_two = two.velocity-(2*one.mass/(one.mass+two.mass))\
        *(((two.velocity-one.velocity).dot(two.position-one.position))/\
            ((two.position-one.position).dot(two.position-one.position)))\
        *(two.position-one.position)

        return [np.around(new_p_one,decimals = 4),np.around(new_p_two,decimals = 4),np.around(new_v_one,decimals = 4),np.around(new_v_two,decimals = 4)]

    def reflection_update(self, one, last_event_time,current_time) -> list:
        "Return each ball's new position and new velocity after reflection"
        "[new_p_one, new_v_one]"
        time_diff = current_time - last_event_time
        #print("TIMEDIFF: ",time_diff)
        # New velocity wrong!!!
        new_p_one = one.position + one.velocity*time_diff
        if one.position.dot(one.position) == 0:
            new_v_one = one.velocity*(-1)
        else:
            new_v_one = one.velocity - 2*((one.velocity.dot(one.position))/(one.position.dot(one.position)))*(one.position)

        return [np.around(new_p_one,decimals = 4), np.around(new_v_one,decimals=4)]

    def updating_sphere(self, all_accident, previous_time, current_time, current_time_increment):
    
        if len(all_accident[current_time]) == 1: # Reflection
                new_set_values = self.reflection_update(all_accident[current_time][0],previous_time,current_time)
                print("im here: ",new_set_values[0])

                # [new_p_one, new_v_one]
        else: #Collision
                new_set_values = self.collision_update(all_accident[current_time][0], all_accident[current_time][1])
                # [new_p_one, new_p_two, new_v_one, new_v_two]

        for i in self.sphere_list:
            if len(all_accident[current_time]) == 2: # Collision: two balls
                # update ball 1
                if(i.name == all_accident[current_time][0].name):
                    i.velocity = new_set_values[2]
                    i.position = new_set_values[0]
                # update ball 2
                elif(i.name == all_accident[current_time][1].name):
                    i.velocity = new_set_values[3]
                    i.position = new_set_values[1]
                # update position
                else:
                    i.position = i.position + i.velocity * current_time_increment

            else: # Reflection: one ball reflected
                # update ball one
                if(i.name == all_accident[current_time][0].name):
                    i.velocity = new_set_values[1]
                    i.position = new_set_values[0]
                # update position
                else:
                    i.position = i.position + i.velocity * current_time_increment

    def run(self):
        
        collided = False
        collide_accident = {}

        for i in range(0, len(self.sphere_list)-1):
            for j in range(i+1, len(self.sphere_list)):
                ij_collide = self.collision(self.sphere_list[i], self.sphere_list[j])
                if (ij_collide): # Collision
                    current_time = self.collide_time(self.sphere_list[i], self.sphere_list[j])
                    collide_accident[current_time] = [self.sphere_list[i], self.sphere_list[j]]
                    collided = True
        if collided == False:
            for i in self.sphere_list:
                 if (self.static(i) == False): # Reflection
                    reflect_time = self.reflect_time(i)
                    collide_accident[reflect_time] = [i]   


        current_least_time = min(collide_accident.keys())
        least_time = current_least_time + self.current_time_track[len(self.current_time_track) - 1] # least_time is CUMULATIVE!
        self.current_time_track.append(least_time)


        self.all_accident[least_time] = collide_accident[current_least_time]
        if len(self.current_time_track) > 1:
            prev_time = self.current_time_track[len(self.current_time_track)-2]
        else:
            prev_time = 0
        self.updating_sphere(self.all_accident, prev_time, least_time, current_least_time)        

        if len(collide_accident[current_least_time]) == 1:
            print(f"time of event: {least_time}\nreflecting {collide_accident[current_least_time][0].name}")
        else:
            print(f"time of event: {least_time}\ncolliding {collide_accident[current_least_time][0].name} {collide_accident[current_least_time][1].name}")

        for i in self.sphere_list:
            print(i.name, "m=",i.mass,"R=",i.radius,f"p=({i.position[0]},{i.position[1]},{i.position[2]})",f"v=({i.velocity[0]},{i.velocity[1]},{i.velocity[2]})")
        print ("energy:", energy(self.sphere_list))
        mv = momentum(self.sphere_list)
        print (f"momentum: ({mv[0]:5.2f},{mv[1]:5.2f},{mv[2]:5.2f})\n")

        # Updating the Universe
        next_time = least_time
        if (next_time <= self.duration):
            self.run()

    def print_initial(self):
        print("\nHere are the initial conditions.\n"
              f"universe radius {self.radius} \n"
              f"end simulation {self.duration}")
        for i in self.sphere_list:
            print(i.name, "m=",i.mass,"R=",i.radius,f"p=({i.position[0]},{i.position[1]},{i.position[2]})",f"v=({i.velocity[0]},{i.velocity[1]},{i.velocity[2]})")
        print ("energy:", energy(self.sphere_list))
        mv = momentum(self.sphere_list)
        print (f"momentum: ({mv[0]:.2f},{mv[1]:.2f},{mv[2]:.2f})")
        print ("\nHere are the events.\n")

def main():
   # Error handling - 2 Command line arguements: time, duration
    if len(sys.argv) != 3:
        print("Please give 2 arguments for time and duration.")
        return

    # Input phase
    print("Please enter the mass, radius, \
x/y/z position, x/y/z velocity\nand name of \
each sphere\nWhen complete, use EOF / Ctrl-D to stop entering")
    spheres = [] 
    while True:
        try:
            line = input()
        except EOFError:
            break
        line_list = line.split()

        # Error handling: Too many or few fields in one line & Invalid mass or radius
        if len(line_list) != 9 or float(line_list[0]) < 0 or float(line_list[1]) < 0:
            exit(1)

        spheres.append(Sphere(float(line_list[0]),float(line_list[1]),\
            float(line_list[2]),float(line_list[3]),float(line_list[4]),\
            float(line_list[5]),float(line_list[6]),float(line_list[7]),\
            line_list[8]))

    w = World(float(sys.argv[1]), float(sys.argv[2]), spheres)
    # Executing phase
    w.print_initial()
    w.run()


if __name__ == '__main__':
    main()