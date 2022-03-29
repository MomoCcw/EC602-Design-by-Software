
import numpy as np
import sys
import math
from itertools import combinations

class Sphere:
    def __init__(self, name, mass, radius, xpos, ypos, zpos, xvel, yvel, zvel):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.pos = np.array((xpos, ypos, zpos))
        self.vel = np.array((xvel, yvel, zvel))


    def overlaps(self, other):
        dist = self.pos - other.pos
        dist_norm = np.linalg.norm(dist)
        return dist_norm <= (self.radius + other.radius)


    def move(self, dt):
        self.pos += self.vel * dt



class World:
    def __init__(self, spheres, radius, TimeLimit, dt):

        self.spheres = spheres
        self.dt = dt
        self.radius = radius
        self.energy = 0
        self.momentum = np.array((0.0, 0.0, 0.0))
        self.time = 0.0
        self.TimeLimit = TimeLimit
        self.initial()

    def getenergy(self):
        self.energy = 0
        for sphere in self.spheres:
            self.energy = self.energy+0.5 * sphere.mass * sum((sphere.vel ** 2))

    def getmomentum(self):
        self.momentum = np.array((0.0, 0.0, 0.0))
        for sphere in self.spheres:
            self.momentum += sphere.mass * sphere.vel



    def new_vel(self, sphere1, sphere2):
        m1=sphere1.mass
        m2=sphere2.mass
        mtotal = m1 + m2
        r1=sphere1.pos
        r2=sphere2.pos
        v1=sphere1.vel
        v2=sphere2.vel
        sphere1.vel = v1 - 2*(m2 / mtotal)*(np.dot(v1-v2, r1-r2)/np.dot((r1-r2),(r1-r2)))* (r1 - r2)
        sphere2.vel = v2 - 2*(m1 / mtotal)*(np.dot(v2-v1, r2-r1)/np.dot((r2-r1),(r2-r1)))* (r2 - r1)

    def collisions(self):
        for i,j in combinations(self.spheres, 2):
            if i.overlaps(j):
                self.new_vel(i, j)
                self.collide(i, j)


    def boundary_collisions(self, p):
        if  math.sqrt(np.dot(p.pos, p.pos.T)) + p.radius < self.radius:
            pass

        else:
            p.vel = p.vel - 2 * (np.dot(p.vel, p.pos) * (p.pos / np.sum(p.pos ** 2)))
            self.reflect(p)


    def run(self):
        while self.energy > 0.0 :
            self.time = self.time+self.dt
            if self.time>=self.TimeLimit:
                return 0
            for i, p in enumerate(self.spheres):
                p.move(self.dt)
                self.boundary_collisions(p)
            self.collisions()
            self.getenergy()

    def initial(self):
        if len(self.spheres) > 0:
            print("Here are the initial conditions.")
            print("universe radius {}".format(self.radius))
            print("end simulation {}".format(self.TimeLimit))
            for sphere in self.spheres:
                s_str = "{} m={} R={} p=({:g},{:g},{:g}) v=({:g},{:g},{:g})".format(sphere.name, sphere.mass, sphere.radius, sphere.pos[0], sphere.pos[1], sphere.pos[2], sphere.vel[0], sphere.vel[1], sphere.vel[2])
                print(s_str)
            self.getenergy()
            self.getmomentum()
            print("energy: {:g}".format(self.energy))
            print("momemtum: ({:g},{:g},{:g})".format(self.momentum[0], self.momentum[1], self.momentum[2]))
            print('\n')
            print("Here are the events.")
            print('\n')

    def reflect(self, sphere):
        if len(self.spheres) > 0:
            print("time of event:{:g}".format(self.time))
            print("reflecting %s" %sphere.name)
            for sphere in self.spheres:
                sphere_info="{} m={} R={} p=({:g},{:g},{:g}) v=({:g},{:g},{:g})".format(sphere.name, sphere.mass, sphere.radius, sphere.pos[0], sphere.pos[1], sphere.pos[2], sphere.vel[0], sphere.vel[1], sphere.vel[2])
                print(sphere_info)
            self.getenergy()
            self.getmomentum()
            print("energy: {:g}".format(self.energy))
            print("momemtum: ({:g},{:g},{:g})".format(self.momentum[0], self.momentum[1], self.momentum[2]))
            print('\n')

    def collide(self, sphere1, sphere2):
        if len(self.spheres) > 0:
            print("time of event: {:g}".format(self.time))
            print("colliding %s %s" %(sphere1.name, sphere2.name))
            for sphere in self.spheres:
                s_str = "{} m={} R={} p=({:g},{:g},{:g}) v=({:g},{:g},{:g})".format(sphere.name, sphere.mass, sphere.radius, sphere.pos[0], sphere.pos[1], sphere.pos[2], sphere.vel[0], sphere.vel[1], sphere.vel[2])
                print(s_str)
            self.getenergy()
            self.getmomentum()
            print("energy: {:g}".format(self.energy))
            print("momemtum: ({:g},{:g},{:g})".format(self.momentum[0], self.momentum[1], self.momentum[2]))
            print('\n')

def Read():
    if len(sys.argv)==3:
        radius = float(sys.argv[1])
        TimeLimit = int(sys.argv[2])
    else:
        return 0

    sphereList = []
    for line in sys.stdin:
        lines = line.split()

        if len(lines) == 9:
            name_=lines[8]
            mass_=float(lines[0])
            radius_=float(lines[1])
            xpos_=float(lines[2])
            ypos_=float(lines[3])
            zpos_=float(lines[4])
            xvel_=float(lines[5])
            yvel_=float(lines[6])
            zvel_=float(lines[7])
            sphere = Sphere(name_, mass_, radius_, xpos_, ypos_, zpos_, xvel_, yvel_, zvel_)
            sphereList.append(sphere)
        else:
            return 0

    dt = 0.0001
    sim = World(sphereList, radius, TimeLimit, dt)
    sim.run()

def main():
    Read()

if __name__ == '__main__':
    main()
