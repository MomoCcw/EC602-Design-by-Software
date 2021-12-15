#include "ec602.hpp"
using namespace ec602;

class MyException: public std::exception {
  public: 
    MyException(string s) {}
};

double divide(int x, int y) {
  double answer;
  if (y==0) {
    throw MyException("divide by zero");
  }

  return 1.0 * x/y;
}

int main(int argc,char** argv) {
  int n;


  try {
   n = std::stoi(argv[1]);
   throw "throw";
   cout << divide(1,4) << "\n";
   cout << divide(1,0) << "\n";
   cout << divide(1,4) << "\n";

  }
  catch (int r) {
    cout << "int\n";
    n = r;
  }
  catch (std::invalid_argument x) {
    cout << "invalid\n";
  } 
  catch (std::exception a) {
   cout << "some exception\n";
  }

  catch (...) {
     cout << "...\n";
  }


  cout << "n: " << n << "\n";
}