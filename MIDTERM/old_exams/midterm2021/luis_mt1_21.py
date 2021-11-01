# Midterm One: python
#
# Please read this entire comment before starting
# the exam.

# The exam starts at 9am ET and ends at 11am ET.
# It is open book, open computer, open internet,
# but you may not collaborate with each other or
# ask other people for help.
#
# This file serves as 
#
# 1. the instructions for the midterm
# 2. a template for you to start your submission
# 3. a description of what is required through test cases
#    in main.
#
# There are two parts to the exam, as follows:
#
# A) The functions "howmany" and "reverse"
# B) The class Vector2D
#
# The detailed specifications of these functions
# and class are contained in the test_ functions
# and in the results of those test_ functions as shown
# below
#
#
# Please complete these functions and classes,
# documenting your work as necessary.
# When you are finished, you can submit the file
# mtone.py with your author information completed
# at
#
#    https://curl.bu.edu:60221/submit_assignment/mtone
#
#
# GRADING
# your submission will be graded on
#  - correctness 
#  - elegance of your solution (simple, easy to read)
# 
# In the case of ties, exams will then be ranked based
# on the time of submission.




# this is the exam. finish these.
import functools

def howmany(s : str, e : str) -> int:
    "how many of the characters in e appear in s"
    e = list(e)
    s = list(s)
    counter = 0
    for index in range(len(e)):
        if e[index] in s:
            counter += 1
    return counter
def reverse(s: str) -> str:
    "convert upper case to lower case and lower case to upper case"
    s = list(s)
    temp_string = ''
    for element in s:
        if element.islower():
            temp_string = temp_string + element.upper()
        elif element.isupper():
            temp_string = temp_string + element.lower()
        else:
            temp_string = temp_string + element
    return temp_string
@functools.total_ordering
class Vector2D:
    "a representation of 2-dim euclidean vectors"
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __add__(self,vector2):
        new_vector = Vector2D(self.x + vector2.get_x(),
            self.y + vector2.get_y())
        return new_vector
    def __sub__(self,vector2):
        new_vector = Vector2D(self.x - vector2.get_x(),
            self.y - vector2.get_y())
        return new_vector
    def __neg__(self):
        self.set_x(-(self.x))
        self.set_y(-(self.y))
    def __mul__(self, vector2):
        if isinstance(vector2,Vector2D):
            new_vector = Vector2D(self.x * vector2.get_x(),
                self.y * vector2.get_y())
            return new_vector
        else:
            new_vector = Vector2D(self.x * vector2, 
                self.y * vector2)
            return new_vector
    __rmul__ = __mul__
    def __eq__(self, vector2):
        if self.x == vector2.get_x() and self.y == vector2.get_y():
            return True
        else:
            return False
    def __lt__(self,vector2):
        return abs(self.x) + abs(self.y) < abs(vector2.get_x()) + abs(vector2.get_y())

    def __str__(self):
        return '[{},{}]'.format(self.x,self.y)
    def __repr__(self):
        return '[{},{}]'.format(self.x,self.y)
    def __matmul__(self,vector2):
        x = self.x * vector2.get_x()    
        y = self.y * vector2.get_y()
        return x + y
    def get_x(self):
        return self.x 
    def get_y(self):
        return self.y
    def set_x(self,x):
        self.x = x 
    def set_y(self,y):
        self.y = y 
        



# the code below can be modified, commented out,
# augmented, etc. Please save this file 
# unmodified as a reference for later.

def test_howmany():
    howmany("abcde","abcde")  #  5
    howmany("ABCDE","abcde")  #  0
    howmany("xxyyzz","xy")    #  2
    howmany("a1343a", "444")  #  1
    howmany("a1343a", "aa")   #  1
    howmany("","123")         #  0
    howmany("1234","")        #  0
    howmany("%","%")          #  1
    howmany("$$","$$")        #  1
    howmany("##@@#","@@@##")  #  2


def test_reverse():
    reverse("abc")    #  "ABC"
    reverse("XYZ")    # "xyz"
    reverse("123")    # "123"
    reverse("ccB bZ") # "CCb Bz"
    #reverse(123)      # raises exception
 

# Note:
# the results are shown in the comments
# simply as x, y 
# instead of Vector2D(x,y) for brevity

def test_vector():
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 5)
    v3 = Vector2D(0.5, -2.1)   
    v4 = Vector2D()            # 0, 0

    v1+v2    # 4, 7
    v2-v1    # 2, 3
    -v3      # -0.5, 2.1
    v1 @ v2  # 13   [this is the dot product]
    v1 * v2  # 3,10 [this is the element-wise product]
    1.2*v1   # 1.2, 2.4
    
    v2 == v1    # False
    v4 == 0*v1  # True

    print(v1, v2, [v3, v4]) # print something *nice*, format up to you

    L=[v1,v2,v3,v4]
    L.sort()        # sort based on the Manhattan distance of the
                    # vectors, i.e. |x| + |y|
                    # result should be L = [v4,v3,v1,v2]
    print(L)


def main():
    """this functions serves as a partial test suite for the exam"""
    test_howmany()
    test_reverse()
    test_vector()


if __name__ == '__main__':
    main()