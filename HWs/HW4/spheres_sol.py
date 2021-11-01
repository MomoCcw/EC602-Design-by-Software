#!/usr/bin/env python
# Copyright 2021 EC602/J Carruthers jbc@bu.edu
#
"""
assignment 4 solution
"""

import sys
import numpy as np

DEBUG=False
def g(x):
    return f"{x:g}"

class Sphere():
    "model a sphere with linear velocity"

    def __init__(self, name, mass, radius, position, velocity):
        self.name = name
        self.pos = position
        self.vel = velocity
        self.mass = mass
        self.radius = radius


    def __str__(s):
       "one m=20 R=1 p=(0,0,94.0839) v=(0,-0.0298792,0.823232)"
       #vform = 
       p = f"({g(s.pos[0])},{g(s.pos[1])},{g(s.pos[2])})"
       v = f"({g(s.vel[0])},{g(s.vel[1])},{g(s.vel[2])})"
       return f"{s.name} m={g(s.mass)} R={g(s.radius)} p={p} v={v}"


    def move(self, deltat):
        "move the sphere"
        self.pos = self.pos + deltat * self.vel

    def reflect_time(self, uni_rad):
        """predict the time of reflection between self
           and the universe, Inf if no valid reflection"""

        a_co = self.vel @ self.vel
        if a_co == 0:
            return np.Inf

        b_co = 2 * self.pos @ self.vel
        c_co = self.pos @ self.pos -  (uni_rad - self.radius)**2
        rootarg = b_co * b_co - 4 * a_co * c_co
        root = rootarg**0.5
        
        refltime = (-b_co + root) / (2 * a_co)
        if abs(refltime)<1e-8:
            return 0
        
        return refltime

    def collide_time(self, two):
        """predict the time of collision between self and two,
           Inf if no valid collision"""
        delr = self.pos - two.pos
        delv = self.vel - two.vel

        a_co = delv @ delv
        if a_co == 0:
            return np.Inf

        dr2 = delr @ delr
        b_co = 2 * delr @ delv
        rootarg = b_co * b_co - 4 * a_co * (dr2 - (self.radius+two.radius)**2)
        if rootarg < 0:
            return np.Inf
        root = rootarg**0.5

        colltime = (-b_co - root) / (2 * a_co)
        if abs(colltime)<1e-8 and (delr @ delv) < 0:
            return 0
        elif colltime > 0:
            return colltime

        return np.Inf



def get_sphere_data():
    "read in the sphere data"
    spheres = []
    for line in sys.stdin:
        try:
            vals = line.split()
            mass,rad = (float(x) for x in vals[:2])
            p = np.array([float(x) for x in vals[2:5]])
            v = np.array([float(x) for x in vals[5:8]])
            name = vals[8]
            spheres.append(Sphere(name, mass, rad, p, v))
        except ValueError:
            return None

    return spheres


def get_next_collision(curr_time, spheres):
    "determine the next collision time for all spheres"
    next_collision = np.Inf
    colliders = None, None
    for i, one in enumerate(spheres):
        for j, two in enumerate(spheres):
            if i >= j:
                continue
            colltime = one.collide_time(two)
            if colltime < next_collision:
                next_collision = colltime
                colliders = i, j

    return colliders, curr_time + next_collision

def get_next_reflection(curr_time, uni_rad, spheres):
    "determine the next reflection time for all spheres"
    next_reflection = np.Inf
    reflector = None

    for i, one in enumerate(spheres):
        refltime = one.reflect_time(uni_rad)
        if refltime < next_reflection:
            next_reflection = refltime
            reflector = i

    return reflector, curr_time + next_reflection

def total_energy(spheres):
    return sum(0.5*s.mass*s.vel@s.vel for s in spheres)

def momentum(spheres):
    return sum(s.mass*s.vel for s in spheres)

def update_position(spheres, deltat):
    "move spheres"
    for s in spheres:
        s.move(deltat)
"""
Here are the collision events.

time of event: 94.0839
colliding one two
one m=20 R=1 p=(0,0,94.0839) v=(0,-0.0298792,0.823232)
two m=2 R=5 p=(0,1,100) v=(0,0.298792,1.76768)
energy: 10
momentum: (0,0,20)
"""


def print_report(curr_time, spheres,**kw):
    if 'conditions' in kw:
        print('universe radius',kw['conditions'][0])
        print('end simulation',kw['conditions'][1])
    else:
        print("\ntime of event:",g(curr_time))

    if 'colliders' in kw:
        print('colliding',*[spheres[x].name for x in kw['colliders']])
    elif 'reflector' in kw:
        print('reflecting',spheres[kw['reflector']].name)

    for s in spheres:
        print(s)
    print(f'energy: {g(total_energy(spheres))}')
    m= momentum(spheres)
    mstr = f"({g(m[0])},{g(m[1])},{g(m[2])})"
    print(f'momentum: {mstr}')



def elastic_collision(one, two):
    """one and two are colliding. update their velocities"""
    hitvec = one.pos - two.pos
    alpha = (one.vel - two.vel) @ hitvec / (hitvec @ hitvec)
    total_mass=one.mass + two.mass
    assert alpha <= 0, "{} {}".format(one, two)
    move_vec = 2*alpha * hitvec /total_mass
    if move_vec.any():
        two.vel += one.mass * move_vec
        one.vel -= two.mass * move_vec


def elastic_reflection(one):
    """one is reflecting. update the velocity"""
    hitvec = one.pos
    alpha = one.vel @ hitvec / (hitvec @ hitvec)
    one.vel = one.vel - 2 * alpha * hitvec


def main():
    "get simulation and report on elastic collisions"
    try:
        universe_radius = float(sys.argv[1])
        end_simulation = float(sys.argv[2])
    except:
        return 1

    spheres = get_sphere_data()

    curr_time = 0
    print("Here are the initial conditions.")
    print_report(curr_time,spheres,conditions=(universe_radius,end_simulation))

    print("\nHere are the events.")

    while True:
        # find the next collision time and spheres involved.
        (one, two), true_col_time = get_next_collision(curr_time, spheres)

        refl, true_wall_time = get_next_reflection(curr_time, universe_radius, spheres)

        if true_col_time > end_simulation and true_wall_time > end_simulation:
            break
        # move all objects to the collision time
        if true_col_time < true_wall_time:
            deltat = true_col_time - curr_time
            update_position(spheres, deltat)
            curr_time = true_col_time

            # record the collision
            elastic_collision(spheres[one], spheres[two])
            print_report(curr_time,spheres,colliders=(one,two))
        else:
            deltat = true_wall_time - curr_time
            update_position(spheres, deltat)
            curr_time = true_wall_time
            elastic_reflection(spheres[refl])
            print_report(curr_time,spheres,reflector=refl)


    return 0


if __name__ == '__main__':
    exit(main())
