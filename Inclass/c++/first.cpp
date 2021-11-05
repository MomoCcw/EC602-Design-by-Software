// About C++
// Our first c++ program

// this is a comment
// using // requires one per line
// everything after a // on a line
//  is a comment, even if it is /* */

/* this is
also a comment
for multiline comments
  */

/* this comment ends */  // now a comment

// What is C++?

//  - compiled
//  - object-oriented (classes)
//  - supports structured programming (functions)
//  - both a high-level language and
//    a low-level language.
//  - it is a superset of the C prog. language.
//     - standard template library (STL: map)
//
//     - classes: methods, data attribute/
//
//  - used for: games, applications like Pages
//      MS Word, operating system, scientific
//      computing, sensing/instrumention
//
//  - part of the C/java family


//  ++ means increment.
//

//
//  low level: close to the details of the
//  computer: access to memory, bit operations
//
//  high level: python, java
//   dictionary, list

//   PYTHON              vs       C++
//   whitespace/newlines          {} () etc
//   define structure             define structure
//                                whitespace is ignored

// What is complete C++ program?
// it is a sequence of declaration statements
//
// one of which must be a declaration of main()


// no code here:

// int x;  // declare an integer
int x = 1;  // assign a value.

// NAMES FOR PUNCUATION

// ( ) parentheses
// { } braces or curly braces
// [ ] brackets
// < > angle brackets
// " " double quote
// ' ' single quote


// ABOUT MAIN

// function name is:  main
// there must be one and only one function main
// this signals the starting point
// of your program when it is run


// ( )  the location where argument can be
//      specified.

// { }  indicate the body of the function,
//      i.e. what we are going to do.

// the word before the function name
// must be a type as defined by the
// language (or user-defined type)
// and it indicates the value that the
// function returns to the calling entity.
//
// What is the body?
//
// a sequence of "statements"
//
// statement1
// statement2
// statement3
// ...
// statementN
//

// python equivalent.
// def main() -> int:
//    body1
//    body2

// STATEMENTS
//
//  - declaration:  define something
//  - expression :  evaluate
//  - jump       :  move execution somewhere else
//  - selection  :  branching
//  - iteration  :  looping for / while
//  - compound   :  a collection of other statements.

// EXPRESSION
//   x+1
//   true
//   f(x) * y
//
// an expression statement is an expression
// followed by a semicolon ;
//

// C++ programs must be compiled
//
//  g++ first.cpp
//    creates a program called a.out


// g++ is silent upon success
//     sends errors to stdout.
//
// redirect stdout to a file
// g++ first.cpp 2> myerrors.txt
//
// NAMING our programs
//
// g++ first.cpp -o first
//
// creates a executable with the name first


// Running
//    a.out in terminal
//    ctrl-B in sublime (input is not handled)
//
//


// as of c++11 return is not required
// in main.

int main() {
// body
// return 42; // a jump statement,
    // immediately exits the function
    // we are "in"

// while (expression)  statement

// while ( true ) {  // while : iteration
//    5+6;           // true : expression
//    'a';           //
// }  // { } convert statement to compound statement



    return 0; // leave in, but it is optional.
} // return in main, is like sys.exit in python
// in python , EOF is also allowed.