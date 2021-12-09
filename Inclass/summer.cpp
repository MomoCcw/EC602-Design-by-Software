// example:
// vector operations
// for loops

// Read in N integers from stdin, output the total.
// N is specified on command line.

#include "ec602.hpp"
using namespace ec602;

int main(int argc, char** argv) {
  if (argc != 2) return 1;
  
  int N = stoi(argc[1]);
  vector<int> v(5,6);
  for (int e : v) {
    cout << e << " ";
  }
  cout << "\n";
  
  for (int i=0; i<N; i++)
    cin >> v[i]
}