# EC602 Midterm One: Python
# Copyright 2019  name email@bu.edu

# you may make a total of 10 point changes
# in the grading scheme.

from random import uniform as w

grade = {'basesix': 10,
         'all_there': 10,
         'kv_match': 10,
         'half_same': 10,
         'Point': 10,
         'Rect': 20,
         'queenmoves': 20,
         'asciisort': 10}

print(sum(grade.values()))


def basesix(x):
    """convert the integer x into a base-6 string representation of x"""
    return "0"


def all_there(pool, fish):
    """return True if every element in the sequence fish exists in the sequence pool, 
    return False otherwise"""


def kv_match(D):
    """for the dictionary D, return the number of keys 
    which are equal to their values"""


def half_same(x):
    """return True if the floating point number x can be represented
    using the half-precision number format (16 bits) without any loss of information.
    Assume that x is a double-precision number (64 bits)"""


class Point():
    """represent a point P(x,y) on the plane"""


class Rect():
    """represent a rectangle on the plane.
    Rect(left,right,bottom,top) is the syntax to create."""


def queenmoves(board):
    """board is 8 line string with representing a chessboard
    with a single queen on the board, marked with the letter Q

    Return a new chess board with the same format, but with
    all places on the chess board that the queen can move to
    marked with an "X"

    A queen can move diagonally, vertically, or horizontally
    an arbitrary number of spaces."""


def asciisort(L):
    """sort the list L according to the numerical(ASCII) values
    of its elements as strings"""


example_board = """********
********
******Q*
********
********
********
********
********"""


def main():
    print('basesix test')
    for i in range(100):
        if int(basesix(i), 6) != i:
            print(f'basesix({i}) is not working')

    print('all_there test')
    print(all_there((1, 2, 3), (3, 4)))       # False
    print(all_there(range(10), range(3, 7)))  # True
    print(all_there("abcd", "BC"))            # False
    print(all_there([], tuple()))             # True
    print(all_there("abcdef", "aaaee"))       # True

    print('kv_match')
    print(kv_match({1: 2, 'a': "a", (1, 2): (1, 2)}))  # 2
    print(kv_match({1: 2, 2: 1}))                      # 0
    print(kv_match({x: x for x in range(100)}))        # 100
    print(kv_match({1: {}, 2: {}, "abc": "abc"}))      # 1

    print('half_same')
    print(half_same(1/5))         # False
    print(half_same(0))           # True
    print(half_same(1023))        # True
    print(half_same(-0.125))      # True
    print(half_same(1.23456789))  # False
    print(half_same(0.5**12))     # True
    print(half_same(100_000))     # False

    print('queenmoves test')
    print(example_board)
    print(repr(example_board))
    print(queenmoves(example_board))

    print('Rect/Point test')
    try:
        special_points = [Point(4, 6), Point(
            5, 8), Point(5, 5), Point(6, 8), Point()]
        r = Rect(4, 6, 1, 8)
        random_points = [Point(w(3.5, 6.5), w(0, 10)) for x in range(10)]
        points = special_points+random_points
        print('testing', points)
        for q in points:
            if q in r:
                print(q, 'is inside of', r)
            else:
                print(q, 'is outside of', r)
        print([r])
    except:
        print('Something is not right with Rect/Point.')
        print('Get rid of try/except to learn more')

    print('asciisort test')
    L = [9, 32, "a", 1, 7, -102, "xyz", 0.1, "0.1", 0.1, "1/10", "X", "\n"]
    print(L)
    n = asciisort(L)
    print(n, L)


if __name__ == '__main__':
    main()
