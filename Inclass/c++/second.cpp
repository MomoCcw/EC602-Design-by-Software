// Our second program
// - declare variables
// - calculate with them (expressions)
// - output

#include<iostream>
using std::cout;
using std::endl;

int main() {
 // declare things;
 char c;       // a single ASCII / utf-8 character
 int i;        // integer
 bool b;       // boolean true / false 
 float f;      // real numbers: 32-bit
 double d;     //               64-bit
 
 // each variable has a type and a name.

 // assign
 c = 'a';
 i = 42;
 b = true;
 f = 3.14259;
 d = 1.23456789;

 // f+d expression
 f  =  f + d;

 // Calculations
 //  need operators: 
 //    "math":       + - / * %  << >>
 //
 //    "bit":      bitand bitor xor
 //                   &     |    ^
 //
 //    "boolean":    and  or    not
 //                  &&   ||      !
 //
 //    "comparison": ==  >  <  >=  <=  !=
 //    "assignment":  =  += *= /= 
 //

 //    "exponentiation": not included in the language
 //           x**y  is python
 //           x^y   is matlab
 //         library (cmath) with pow() functions

 
 // Output
 // cout is a variable (object) defined by iostream
 //      it is connected to stdout of  terminal
 //
 //  << is defined to mean "send to"
 //
 // std is the namespace used by the C++ libraries
 // :: is an operator and it is called.
 
 // in python
 // import iostream as std
 //  std.cout

 std::cout << f << '\n';


 cout << c << " " << i << " " << d << " " << b << "\n";

 if (c) cout << "c is true \n";
 b = true;
 if ((b = false)) {
    cout << "b is false\n";
 }
 else {
    cout << "b is not false\n";
 }
}