# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# Copyright 2021 Zhaozhong Qi zqi5@bu.edu

import numpy as np
import math
import sys

class World:
    def __init__(self, radius, duration, spheres):
        self.radius = radius
        self.duration = duration
        self.velocity = np.array([0,0,0])
        self.position = np.array([0,0,0])
        self.sphere_list = spheres

    def collide(self, one, two) -> bool:
        velocity_1 = one.velocity
        position_1 = one.position
        velocity_2 = two.velocity
        position_2 = two.position
        if ((position_2 - position_1).dot(velocity_2 - velocity_1)) < 0:
            return True
        else:
            # They touch each other
            if (position_2 - position_1).dot(velocity_2 - velocity_1) == 0:
                return False
            else:
                return False
    def reflect(self, one) -> bool:
        velocity_1 = one.velocity
        position_1 = one.position
        if (velocity_1[0] == 0) & (velocity_1[1] == 0) & (velocity_1[2] == 0):
            return False
        else:
            return True

    

    def run(self):
        pass

class Sphere:
    def __init__(self,mass,radius,p_x,p_y,p_z,v_x,v_y,v_z,name):
        self.mass = mass
        self.radius = radius
        self.name = name
        self.velocity = np.array([v_x,v_y,v_z])
        self.position = np.array([p_x,p_y,p_z])

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

def collide_time(one,two):
    p_new = two.position - one.position
    v_new = two.velocity - one.velocity
    radius_sum = one.radius + two.radius
    #  a*t^2 + b*t + c = 0
    a = np.linalg.norm(v_new)**2
    b = 2*p_new.dot(v_new)
    c = np.linalg.norm(p_new)**2 - radius_sum**2
    return quadratic_solve(a,b,c)

def reflect_time(one,world):
    p_new = one.position - world.position
    v_new = one.velocity - world.velocity
    radius_diff = world.radius - one.radius
    #  a*t^2 + b*t + c = 0
    a = np.linalg.norm(v_new)**2
    b = 2*p_new.dot(v_new)
    c = np.linalg.norm(p_new)**2 - radius_diff**2
    return quadratic_solve(a,b,c)

def collision(one,two,last_event_time) -> list:
    "Return each ball's new position and new velocity after collision"
    "[new_p_one, new_p_two, new_v_one, new_v_two]"

    time_diff = collide_time(one,two) - last_event_time
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

    return [new_p_one,new_p_two,new_v_one,new_v_two]

def reflection(one,world,last_event_time):
    "Return each ball's new position and new velocity after reflection"
    "[new_p_one, new_v_one]"

    time_diff = reflect_time(one,world) - last_event_time
    new_p_one = one.position + one.velocity*time_diff

    new_v_one = one.velocity - (2*((one.velocity.dot(new_p_one))/(new_p_one.dot(new_p_one)))*(new_p_one))

    return [new_p_one,new_v_one]

def energy(world):
    accum = 0
    for i in world.sphere_list:
        accum += 0.5*i.mass*(np.linalg.norm(i.velocity)**2)
    return accum

def momentum(world):
    accum = np.array([0,0,0])
    for i in world.sphere_list:
        accum = accum + (i.velocity*i.mass)
    return accum

def print_initial(world):
    print("Here are the initial conditions.\n"
          f"universe radius {world.radius} \n"
          f"end simulation {world.duration}")
    for i in world.sphere_list:
        print(i.name, "m=",i.mass,"R=",i.radius,f"p=({i.position[0]},{i.position[1]},{i.position[2]})",f"v=({i.velocity[0]},{i.velocity[1]},{i.velocity[2]})")
    print ("energy:", energy(world))
    mv = momentum(world)
    print (f"momentum: ({mv[0]:5.2f},{mv[1]:5.2f},{mv[2]:5.2f})")
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

    # Executing phase
    world = World(float(sys.argv[1]),float(sys.argv[2]),spheres)
    world.run()

    print_initial(world)


if __name__ == '__main__':
    main()


