
#include "ec602.hpp"
using namespace ec602;


/*
 functions
  
type name(declarations of arguments) {
    body
    return value;
}
*/

// pass by value
int twice(int x) {
    x = 1+x;
    cerr << &x << "\n";
    return 2*x;
}

// alternatives to this:
// needs:
//   multiple return values.
//   modifying your arguments.
// 


// ampersand &
//  in a declaration, it means reference
//  in an expression it means address of.

void multiply(int &w, int n) {
  w = n*w;
  return;
}

int helper(vector<int> h) {
 return 0;
}
// this copies the vector.
int summer(const vector<int> & v) {
 helper(v);
 int total=0;
 for (auto e : v)
    total += e;
 return total;
 // not allowed. v[0]=1;
}

int main(int argc, char** argv) {
  int w=8;
  int z;
  cout << &w << "\n";
  z = twice(w);
  cout << z << "\n";

  // reference variable
  int& rz=z;

  cout << rz << "\n";
  cout << "where" << &z << " " << &rz << "\n";

  multiply(rz, w);
  cout << rz << "\n";

  vector<int> myvals(10000);
  cout << summer(myvals) << "\n";
}