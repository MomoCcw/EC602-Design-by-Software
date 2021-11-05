// Copyright 2021 jbc@bu.edu
//
// Quadratic: a program to calculate the solutions to
// the quadratic equation
//  ax^2 + bx + c = 0
//
// This program should ask the user for three values (a, b, and c)
// and output the solution(s) for x.

// version 0: just do the input and output, leaving the math for later
// version 1: dont worry about complex solutions
// version 2: print out an error message if solutions are complex
// version 3: correctly compute and output complex solutions

// Topics
//   - input and output
//   - terminal streams
//   - storing data with numerical variables
//   - making decisions: branching
//   - assignment operator
//   - mathematics: operators, parentheses.
//   - return codes
//   - the std:: namespace
//   - conditions: booleans and logic operators

// stdin is  cin object
// stdout is cout object
// c means console

// this is not allowed and is a terrible idea.
// pollutes the namespace
// using namespace std;

// boost, sfml, etc.

#include "ec602.hpp"
#include <cmath>

int main() {
  double a, b, c;
  double root1, root2;
  root1 = root2 = 0;

  double disc;
  double real,imag;

  cout << "Enter a, b, and c for quadratic solution: ";

  cin >> a;
  // cout << "done with a\n";
  cin >> b >> c;

  // (-b +/- sqrt(b^2 -4ac))/(2a)

  disc = b * b - 4 * a * c;
  if (disc >= 0) {
    root1 = (-b - std::sqrt(disc)) / (2 * a);
    root2 = (-b + std::sqrt(disc)) / (2 * a);
    cout << "The roots are " << " " << root1 << " and " << root2 << "\n";
  } else {
    imag = std::sqrt(-disc)/(2*a);
    real = -b/(2*a);
    cout << "The roots are " << real << " + j" << imag << " and " << real << " - j" << imag << "\n";
  }

  return 0;
}