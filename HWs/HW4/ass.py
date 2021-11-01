import numpy as np
import math

class Sphere:
    def __init__(self, mass, radius, p_x, p_y, p_z, v_x, v_y, v_z, name):
        self.mass = mass
        self.radius = radius
        self.name = name
        self.velocity = np.array([v_x, v_y, v_z])
        self.position = np.array([p_x, p_y, p_z])

a = Sphere(0,0,0,0,0,0,0,0,'one')
b = Sphere(0,0,0,0,0,0,0,0,'two')
c = Sphere(0,0,0,0,0,0,0,0,'thr')
d = Sphere(0,0,0,0,0,0,0,0,'fou')

spheres = {12.23:[a,b],23.42:[c]}
spherelist = [a,b,c,d]

for i in range(0, len(spherelist)-1):
    for j in range(i+1, len(spherelist)):
        print(spherelist[i].name,spherelist[j].name)

        # collide = self.collision(spheres[i], spheres[j])
        # if (collide == True): # Collision
        #     current_time = self.collide_time(spheres[i], spheres[j])
        #     collide_accident[current_time] = [spheres[i], spheres[j]]
        #     collided = True



def collision(one, two) -> bool:
    if ((two.position - one.position).dot(two.velocity - one.velocity)) < 0:
        return True
    else:
        return False

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

def reflect_time(one):
    p_new = one.position - np.array([0,0,0])
    v_new = one.velocity - np.array([0,0,0])
    radius_diff = 100 - one.radius
    #  a*t^2 + b*t + c = 0
    a = np.linalg.norm(v_new)**2
    b = 2*p_new.dot(v_new)
    c = np.linalg.norm(p_new)**2 - radius_diff**2
    return quadratic_solve(a,b,c)

one = Sphere(0,0,0,0,0,0,0,0,'one')
two_init = Sphere(1,1,1,1,1,1,1,1,"two")
two = Sphere(1,1,692.243,692.243,692.243,-1,-1,-1,'two')

print(reflect_time(two_init))# Two reflect
print(reflect_time(two_init)+collide_time(two,one)) # One Two collide
print(((two.position - one.position).dot(two.velocity - one.velocity)))

# Here One Two Collide is not recorded!!
collided = False
collide_accident = {}
sphere_list = [one,two]

for i in range(0, len(sphere_list)-1):
    for j in range(i+1, len(sphere_list)):
        ij_collide = collision(sphere_list[i], sphere_list[j])
        if (ij_collide): # Collision
            current_time = collide_time(sphere_list[i], sphere_list[j])
            collide_accident[current_time] = [sphere_list[i], sphere_list[j]]
            collided = True
if collided == False:
    for i in sphere_list:
         if (static(i) == False): # Reflection
            reflect_time = reflect_time(i)
            collide_accident[reflect_time] = [i]

for i in collide_accident:
    if len(collide_accident[i]) == 2:
        print(reflect_time(two_init) + i, collide_accident[i][0].name,collide_accident[i][1].name)
    else:
        print(reflect_time(two_init) + i, collide_accident[i][0].name)
def elastic_reflection(one):
    """one is reflecting. update the velocity"""
    hitvec = one.position
    print("asd",one.velocity)
    alpha = one.velocity @ hitvec / (hitvec @ hitvec)
    one.velocity = one.velocity - 2 * alpha * hitvec
    return one.velocity

def reflection_update(one, last_event_time) -> list:
    "Return each ball's new position and new velocity after reflection"
    "[new_p_one, new_v_one]"
    # New_position_one is wrong .!!
    time_diff = reflect_time(one) - last_event_time
    print("TIMEDIFF: ",time_diff)
    new_p_one = one.position + one.velocity*time_diff
    if one.position.dot(one.position) == 0:
        new_v_one = one.velocity*(-1)
    else:
        new_v_one = one.velocity - 2*((one.velocity.dot(one.position))/(one.position.dot(one.position)))*(one.position)

    return [np.around(new_p_one,decimals = 4), np.around(new_v_one,decimals=4)]


print()
one = Sphere(3.1,1.2,4.1,-4.1,4.0,-1.2,5,1,'tennis')
print(reflect_time(one))
print(elastic_reflection(one))
print(reflection_update(one,0))