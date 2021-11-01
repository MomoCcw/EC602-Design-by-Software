import string

def howmany(s : str, e : str) -> int:
    "how many of the characters in e appear in s"
    count = 0
    buffer = []
    for i in e:
        for j in s:
            if i == j and i not in buffer:
                buffer.append(i)
                count += 1
                break
    return count

def reverse(s: str) -> str:
    "convert upper case to lower case and lower case to upper case"
    try:
        s = list(s)
    except:
        return
    buffer = ''
    for i in range(len(s)):
        if s[i].isupper():
            buffer= buffer+s[i].lower()
        elif s[i].islower():
            buffer = buffer + s[i].upper()
        else:
            buffer = buffer + s[i]
    return buffer

class Vector2D:
    "a representation of 2-dim euclidean vectors"
    def __init__(self,x=0,y=0):
        self.x = x 
        self.y = y 
    def __add__(self,other):
        buffer = Vector2D(self.x+other.x,self.y+other.y)
        return buffer
    def __sub__(self,vector2):
        new_vector = Vector2D(self.x - vector2.x,self.y - vector2.y)
        return new_vector
    def __str__(self):
        return '[{},{}]'.format(self.x,self.y)
    def __neg__(self):
        buffer = Vector2D(-self.x,-self.y)
        self.x = -self.x
        self.y = -self.y
        return buffer

    def __mul__(self, vector2):
        if isinstance(vector2,Vector2D):
            new_vector = Vector2D(self.x * vector2.x,
                self.y * vector2.y)
            return new_vector
        else:
            new_vector = Vector2D(self.x * vector2, 
                self.y * vector2)
            return new_vector
    __rmul__ = __mul__
    def set_x(self,x):
        self.x = x 
    def set_y(self,y):
        self.y = y
    def __matmul__(self,vector2):
        x = self.x * vector2.x    
        y = self.y * vector2.y
        buffer = self.x * vector2.x + self.y * vector2.y
        return buffer
    def __eq__(self, vector2):
        if self.x == vector2.x and self.y == vector2.y:
            return True
        else:
            return False
    def __lt__(self,vector2):
        return abs(self.x) + abs(self.y) < abs(vector2.x) + abs(vector2.y)

    def __str__(self):
        return '[{},{}]'.format(self.x,self.y)
    def __repr__(self):
        return '[{},{}]'.format(self.x,self.y)

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 5)
v3 = Vector2D(0.5, -2.1)   
v4 = Vector2D()            # 0, 0

print(v1+v2)   # 4, 7
print(v2-v1)    # 2, 3
print(-v3)     # -0.5, 2.1
print(v1 @ v2)  # 13   [this is the dot product]
print(v1 * v2)  # 3,10 [this is the element-wise product]
print(1.2*v1)  # 1.2, 2.4

v2 == v1    # False
v4 == 0*v1  # True