# reading from stdin all at once

# import sys
# entire_file = sys.stdin.read()
# print(f"{entire_file=}")

# reading from stdin by line
import sys
entire_file = sys.stdin.readlines()
print(f"{entire_file=}")