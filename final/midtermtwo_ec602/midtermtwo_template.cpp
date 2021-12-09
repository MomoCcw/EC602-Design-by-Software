// Copyright 2020 jbc@bu.edu
// 

// RULES:
//  - brackets are allowed
//  - iostream, string, vector can be included, nothing else.
//  - your program should compile as submitted (main() must be here)
//  - astyle and cpplint will not be used, but I
//    may read and evaluate your code as part of the grade


// you may add more using statements, but not more includes.
#include<iostream>
#include<string>
#include<vector>
using std::string;
using std::vector;



// ---------------VISTANCE----------------

/*

Distance Between Two Vectors (vistance)
---------------------------------------


Given two vectors of integers which are
re-arrangements of each other, write
a function to find
the distance between the
locations (ie. the difference of their
index values) of the matching elements.

Example:

vistance({3,9,5},{5,3,9}) = 4

because 3 has been moved 1 spot, 9 moved 1 spot , and 5 moved 2 spots


vistance({2,5,3},{5,2,3}) = 2

because 2 and 5 are each 1 away from
where they are in the other vector

vistance({42,12},{42,12}) = 0

because the values are in the same locations
in each vector.

If the vectors are not
re-arrangements of each other,
throw the string "vistance is an illusion"

extra credit: make it fast.

You may assume that the elements
are unique.

The function signature for vistance() must not be modified.



*/

// ADD YOUR CODE HERE

// template for vistance

int vistance(const vector<int> &a, const vector<int> &b) {
  // a = [1,2,3]; b = [3,2,1]
  return 0; // placeholder return, change it to correct value
}

// ----------------------SUMPARSER

/*
Write a class SumParser that analyses strings
containing the additions and subtractions
of integers written in a base from 2 to 10.

The string will have no spaces and only integer values.

There will never be back-to-back
+ and - symbols.

The main program is already written, you can use it as is
or modify it as desired. However, the constructor and two methods 
that main() references must be implemented such that this version 
of main will still work.

In this main, the base and the string-to-be-evaluated are entered
on a line, then the result of the evaluation is printed as an int (in base
10) and then as a string in the base specified.

*/
// template for SumParser  (intentionally left blank)

class SumParser {
  public:
    string _s;
    int _base;
    SumParser(string, int);
    int get_value();
    string show_result();
}

SumParser::SumParser(string s, int base) {
  _s = s;
  _base = base;
}




// MAIN
// I will ignore code below // MAIN and replace it with my own
// test code.


int main() {
  // test code for SumParser
  // this test code is pretty complete and does not
  // need modification

  std::string s;
  int base;
  while (std::cin >> base >> s) {
    SumParser a{s, base};
    try {
      std::cout << a.get_value() << " "
                << a.show_result() << "\n";
    } catch (...) {
      std::cout << "invalid\n";
    }
  }

  // test code for vistance
  // this is very bare-bones, you will want to do more testing

  //return vistance({3, 6, 9}, {9, 3, 6});
  return 0;
}
