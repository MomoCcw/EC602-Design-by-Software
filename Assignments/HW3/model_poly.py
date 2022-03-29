#!/usr/bin/env python
# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# Copyright 2021 Zhaozhong Qi zqi5@bu.edu

class Polynomial():
    def __setitem__(self, key, value):
        if key in self.my_data:
            self.my_data[key] = value
        else:
            self.my_data.update({key: value})

    def __getitem__(self, key):
        if key < len(self.sequence):
            return self.sequence[key]
        return 0

    def __init__(self, sequence=0):
        'Store the sequence in a dictionary'
        # handling empty input
        if not sequence:
            self.my_data = {}
            return

        # Type check
        if type(sequence) == int:
            self.sequence = [sequence]
        else:
            self.sequence = list(sequence)
            self.sequence.reverse()

        # key is the power, value is the coefficient
        self.my_data = {}
        for i in range(len(self.sequence)):
            self.my_data.update({i: self.sequence[i]})

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.my_data == other.my_data
        return False

    def __add__(self, other_polynomial):
        new_data = self.my_data.copy()
        # Search Values(Coefficient) by Keys(Power) in adding dictionnary
        for key in other_polynomial.my_data:
            # " If same power exist in Polynomial"
            if key in self.my_data:
                new_data.update(
                    {key: (self.my_data[key] + other_polynomial.my_data[key])})
            else:
                new_data.update({key: other_polynomial.my_data[key]})
        buffer = Polynomial()
        buffer.my_data = new_data
        return buffer

    def __repr__(self):
        return format(self.my_data)

    def __sub__(self, other_polynomial):
        new_data = self.my_data.copy()
        # Search Values(Coefficient) by Keys(Power) in adding dictionnary
        for key in other_polynomial.my_data:
            # " If same power exist in Polynomial"
            if key in self.my_data:
                new_data.update(
                    {key: (self.my_data[key] - other_polynomial.my_data[key])})
            else:
                new_data.update({key: other_polynomial.my_data[key]})
        buffer = Polynomial()
        buffer.my_data = new_data
        return buffer

    def deriv(self):
        new_data = {}
        for i in self.my_data:
            if i != 0:
                new_data.update({i-1: i*self.my_data[i]})
        buffer = Polynomial()
        buffer.my_data = new_data
        return buffer

    def eval(self, sub) -> int:
        accum = 0
        for i in self.my_data:
            accum += self.my_data[i]*(sub**i)
        return accum

    def __mul__(self, other):
        left = {}
        right = {}
        for key_left in self.my_data:
            left = {}
            for key_right in other.my_data:
                # For multiply, Sum up the power, multiply with the coefficients
                # First step: Sum up the power
                new_left_key = key_right + key_left
                # Second step: Using key(power) access coefficient respectively, then multiply them
                new_left_value = self.my_data[key_left] * other.my_data[key_right]
                left.update({new_left_key: new_left_value})
                if new_left_key in right:
                    right.update(
                        {new_left_key: right[new_left_key] + new_left_value})
                else:
                    right.update({new_left_key: new_left_value})

        buffer = Polynomial()
        for i in right:
            buffer[i] = right[i]
        return buffer

if __name__ == "__main__":
    p = Polynomial([5,4])
    q = Polynomial()
    print(p)
