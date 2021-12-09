# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# Copyright 2021 Zhaozhong Qi zqi5@bu.edu

def left_rotate(l, n):
    "left rotate a string by n (CounterClockwise)"
    return l[n:] + l[:n]


def right_rotate(l, n):
    "right rotate a string by n (Clockwise)"
    return l[-n:] + l[:-n]


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

    # From left to right, iterate through them cumulatively, i.e. 'a ab abc abcd'
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
    "Based on the original arrangement, return all new arranges when a new person seats in"
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
    divided = []
    for i in range(len(bars)):
        if i != len(bars) - 1:
            divided.append(guests[bars[i]:bars[i+1]])
        else:
            divided.append(guests[bars[i]:]+guests[:bars[0]])
    return divided


def countem(upper_limit: list, values: list):
    current = [0] * len(upper_limit)
    while True:
        temp_string = ""
        for i in range(len(current)):
            temp_string = temp_string + values[i][current[i]]
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
    def __init__(self):
        self.names = []

    def shuffle(self, guests: str) -> list:
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
        # Initialize some data structures
        arranges = []
        divided_linear = []
        permutations = []
        upper_limit = []

        # Divide guests up and find their linears
        divided = divide_str(guests, bars)
        for i in divided:
            divided_linear.append(find_linears(i))
        # Find upper limit (len of each element) of divided_linear (list of list of str)
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


def show_result(v, partial=False):
    v.sort()
    print("", len(v), "\n".join(v), sep="\n")


if __name__ == '__main__':
    standard = Wedding()
    res = standard.shuffle("abcde")
    show_result(res)
    res = standard.barriers("abcd", [2])
    show_result(res)
