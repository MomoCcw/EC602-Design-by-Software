# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# Copyright 2021 Zhaozhong Qi zqi5@bu.edu

# ===========START OF STUDENT'S CODE================
"2021FALL EC602 HW5"


def left_rotate(string, num):
    "left rotate a string by num (CounterClockwise)"
    return string[num:] + string[:num]


def right_rotate(string, num):
    "right rotate a string by num (Clockwise)"
    return string[-num:] + string[:-num]


def linear(orig: str, modified: str) -> bool:
    "Check if one arrangement is linear, i.e. barriers at the ends"
    orig = list(orig)
    modified = list(modified)
    for i in orig:
        if abs(orig.index(i) - modified.index(i)) > 1:
            return False
    return True


def valid(orig: str, modified: str) -> bool:
    "Check if one arrangement is valid, i.e. follow the Wedding seating rules"
    orig = list(orig)
    modified = list(modified)
    for i in orig:
        index_diff = abs(orig.index(i) - modified.index(i))
        if index_diff > 1 and index_diff != (len(orig) - 1):
            return False
    return True


def find_linears(guests: str) -> list:
    "Find all the linear arranges for the given str"
    # If only one or empty guests, return it or None
    if len(guests) == 1:
        return [guests[0]]
    if len(guests) == 0:
        return None

    # Initialize some data structures
    linear_list = [guests[0]]

    # From left to right, iterate through them cumulatively,
    # i.e. 'a ab abc abcd'
    for i in range(1, len(guests)):
        buffer = []
        orig = guests[0:i] + guests[i]

        # Linear_list contains all prev. linear arranges
        for j in linear_list:
            new_arranges = add_person(j, guests[i])

            # Get rid of non-linear arranges.
            for k in new_arranges:
                if linear(orig, k):
                    buffer.append(k)

        linear_list = list(set(buffer))
    return sorted(linear_list)


def add_person(orig: str, adder: str) -> list:
    "Based on the original arrangement, \
    return all new arranges when a new person seats in"
    # 1. stay
    one = orig + adder

    # 2. swap w/ tail
    two = list(one)
    two[len(two)-1], two[len(two)-2] = two[len(two)-2], two[len(two)-1]
    two = "".join(two)

    # 3. swap w/ head
    thr = list(one)
    thr[len(thr)-1], thr[0] = thr[0], thr[len(thr)-1]
    thr = "".join(thr)

    # 4. swap w/ head & cw rotate
    four = list(one)
    four = right_rotate(four, 1)
    four = "".join(four)

    # 5. swap w/ tail & ccw rotate
    five = list(one)
    five = left_rotate(five, 1)
    five = "".join(five)

    ans = [one, two, thr, four, five]
    return ans


def divide_str(guests: str, bars: list) -> list:
    "Divide a string up between barriers"
    divided = []
    for i, val in enumerate(bars):
        if i != len(bars) - 1:
            divided.append(guests[val:bars[i+1]])
        else:
            divided.append(guests[val:]+guests[:bars[0]])
    return divided


def countem(upper_limit: list, values: list):
    "Return all the permutations"
    current = [0] * len(upper_limit)
    while True:
        temp_string = ""
        for i, val in enumerate(current):
            temp_string = temp_string + values[i][val]
        yield temp_string
        j = 0
        current[j] += 1
        while current[j] == upper_limit[j]:
            current[j] = 0
            j += 1
            if j == len(upper_limit):
                return
            current[j] += 1


class Wedding:
    "The assignment: wedding class"
    def __init__(self):
        pass

    def shuffle(self, guests: str) -> list:
        "Return all possible seating arrangements"
        # If only one or empty guests, return it or None
        if len(guests) == 1:
            return [guests[0]]
        if len(guests) == 0:
            return None

        arranges = []

        # Find prev. linear arranges
        linear_list = find_linears(guests[0:len(guests)-1])

        # For each prev. linear arranges, add the last person
        for j in linear_list:
            new_arranges = add_person(j, guests[len(guests)-1])

            # Get rid of invalid arranges.
            for k in new_arranges:
                if valid(guests, k):
                    arranges.append(k)

        return sorted(list(set(arranges)))

    def barriers(self, guests: str, bars: list) -> list:
        "Return all possible seating arrangements w/ barriers"
        # Initialize some data structures
        arranges = []
        divided_linear = []
        permutations = []
        upper_limit = []

        # Divide guests up and find their linears
        divided = divide_str(guests, bars)
        for i in divided:
            divided_linear.append(find_linears(i))
        # Find upper limit (len of each element) of divided_linear
        for i in divided_linear:
            upper_limit.append(len(i))
        # Find permutations in divided_linear
        for i in countem(upper_limit, divided_linear):
            permutations.append(i)
        # Format adjusting
        for i in permutations:
            i = right_rotate(i, bars[0])
            offset = 0
            for j in bars:
                i = i[:j+offset] + '|' + i[j+offset:]
                offset += 1
            arranges.append(i)
        return arranges

# ===========END OF STUDENT'S CODE================


def show_result(v, partial=False, ind=None):
    v.sort()
    if not partial:
        print("", len(v), "\n".join(v), sep="\n")
    else:
        print("", len(v), v[ind], sep="\n")


def standard_tests():
    standard = Wedding()
    res = standard.shuffle("abc")
    show_result(res)

    res = standard.shuffle("WXYZ")
    show_result(res)

    res = standard.barriers("xyz", [0])
    show_result(res)

    res = standard.shuffle("abc")
    show_result(res)

    res = standard.shuffle("abcdefXY")
    show_result(res)

    res = standard.barriers("abcDEFxyz", [2, 5, 7])
    show_result(res)

    res = standard.barriers("ABCDef", [4])
    show_result(res)

    res = standard.barriers("bgywqa", [0, 1, 2, 4, 5])
    show_result(res)

    res = standard.barriers("n", [0])
    show_result(res)
    res = standard.shuffle("hi")
    show_result(res)


def main():

    print("""Type quit to exit.
Commands:
tests
s guests
b guests n barriers
sp guests ind
bp guests n barriers ind
""")
    w = Wedding()
    while True:
        asktype = input().split()
        if asktype[0] == "quit":
            break
        elif asktype[0] == "tests":
            standard_tests()
        elif asktype[0] == "s":
            guests = asktype[1]
            r = w.shuffle(guests)
            show_result(r)
        elif asktype[0] == "b":
            guests, nbar, bars = asktype[1], asktype[2], asktype[3:]
            r = w.barriers(guests, [int(x) for x in bars])
            show_result(r)
        elif asktype[0] == "sp":
            guests, ind = asktype[1:]
            r = w.shuffle(guests)
            show_result(r, True, int(ind))
        elif asktype[0] == "bp":
            guests, nbar, bars, ind = asktype[1], \
                asktype[2], asktype[3:-1], asktype[-1]
            r = w.barriers(guests, [int(x) for x in bars])
            show_result(r, True, int(ind))


if __name__ == '__main__':
    main()
