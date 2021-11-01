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
    reverse(123)      # raises exception
 

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


def main():
    """this functions serves as a partial test suite for the exam"""
    test_howmany()
    test_reverse()
    test_vector()


if __name__ == '__main__':
    main()