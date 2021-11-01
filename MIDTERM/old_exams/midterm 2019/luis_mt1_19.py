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
    string = ''
    while(True):
        string = string[:0] + str(x%6) + string[0:]
        x = int(x/6)
        if x == 0:
            string = string[:0] + str(x%6) + string[0:]
            break
    return string


def all_there(pool, fish):
    pool = list(pool)
    fish = list(fish)
    for elem in fish:
        if not(elem in pool):
            return False
    return True

def kv_match(D):
    """for the dictionary D, return the number of keys 
    which are equal to their values"""
    counter = 0
    for key in D:
        if key == D[key]:
            counter += 1
    return counter

'''
def half_same(x):
    """return True if the floating point number x can be represented
    using the half-precision number format (16 bits) without any loss of information.
    Assume that x is a double-precision number (64 bits)"""
    if isinstance(x,int):
        if x < 65504:
            return True
        else:
            return False
    elif not isinstance(x,float):
        return False
    else:
'''

class Point():
    """represent a point P(x,y) on the plane"""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x 
    def get_y(self):
        return self.y

class Rect():
    """represent a rectangle on the plane.
    Rect(left,right,bottom,top) is the syntax to create."""
    def __init__(self,left,right,bottom,top):
        self.l_left = [0,0]
        self.u_left = [0,bottom+top]
        self.l_right = [left+right,0]
        self.u_right = [left+right,bottom+top]
    def __contains__(self,point):
        if point.get_x() < 0 or point.get_x() > self.l_right[0]:
            return False
        elif point.get_y() < 0 or point.get_y() > self.u_right[1]:
            return False
        else:
            return True
def queenmoves(board):
    """board is 8 line string with representing a chessboard
    with a single queen on the board, marked with the letter Q

    Return a new chess board with the same format, but with
    all places on the chess board that the queen can move to
    marked with an "X"

    A queen can move diagonally, vertically, or horizontally
    an arbitrary number of spaces."""
    board_matrix = [[0 for x in range(8)] for y in range(8)]
    queens_position = [0,0]
    board_string = ""
    i_counter = 0
    j_counter = 0
    
    for i in board:
        if i == '\n':
            i_counter += 1
            j_counter = 0
            continue
        elif i == 'Q':
           board_matrix[i_counter][j_counter] = 1
           queens_position[0] = i_counter
           queens_position[1] = j_counter
           break
        else:
            j_counter += 1 
    print(queens_position)
    # Move Diagonally
        # Before Queen
    temp = queens_position.copy()
    for i in range(min(queens_position[0],queens_position[1])):
        board_matrix[temp[0] - 1][temp[1] - 1] = 1
        temp[0] = temp[0] - 1
        temp[1] = temp[1] - 1
        # After Queen
    temp = queens_position.copy()
    for i in range( 7 - max(queens_position[0], queens_position[1])):
        board_matrix[temp[0] + 1][temp[1] + 1] = 1
        temp[0] = temp[0] + 1
        temp[1] = temp[1] + 1
    # Move Vertically
    for i in range(8):
        board_matrix[i][queens_position[1]] = 1
    # Move Horizontally
    for j in range(8):
        board_matrix[queens_position[0]][j] = 1
    # Matrix -> String
    for i in range(8):
        for j in range(8):
            position = board_matrix[i][j]
            if position == 0:
                board_string = board_string + '*' 
            if position == 1:
                if i == queens_position[0] and j == queens_position[1]:
                    board_string = board_string + 'Q' 
                else:
                    board_string = board_string + 'X'          
            if j == 7:
                board_string = board_string + "\n"
                continue
    return board_string

def asciisort(L):
    """sort the list L according to the numerical(ASCII) values
    of its elements as strings"""
    L.sort(key=lambda x: ord(str(x)[0]))
    return L

example_board = """********
********
******Q*
********
********
********
********
********"""


def main():
    print('basesix test')                                      #DONE
    for i in range(100):
        if int(basesix(i), 6) != i:
            print(f'basesix({i}) is not working')

    print('all_there test')                                    #DONE
    print(all_there((1, 2, 3), (3, 4)))       # False
    print(all_there(range(10), range(3, 7)))  # True
    print(all_there("abcd", "BC"))            # False
    print(all_there([], tuple()))             # True
    print(all_there("abcdef", "aaaee"))       # True

    print('kv_match')                                          #DONE
    print(kv_match({1: 2, 'a': "a", (1, 2): (1, 2)}))  # 2
    print(kv_match({1: 2, 2: 1}))                      # 0
    print(kv_match({x: x for x in range(100)}))        # 100
    print(kv_match({1: {}, 2: {}, "abc": "abc"}))      # 1

    '''
    print('half_same')
    print(half_same(1/5))         # False
    print(half_same(0))           # True
    print(half_same(1023))        # True
    print(half_same(-0.125))      # True
    print(half_same(1.23456789))  # False
    print(half_same(0.5**12))     # True
    print(half_same(100_000))     # False
    '''
    print('queenmoves test')
    print(example_board)
    print(repr(example_board))
    print(queenmoves(example_board))

    print('Rect/Point test')                                    #DONE
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

    print('Something is not right with Rect/Point.')
    print('Get rid of try/except to learn more')

    print('asciisort test')                                     #DONE
    L = [9, 32, "a", 1, 7, -102, "xyz", 0.1, "0.1", 0.1, "1/10", "X", "\n"]
    print(L)
    n = asciisort(L)
    print(n, L)


if __name__ == '__main__':
    main()