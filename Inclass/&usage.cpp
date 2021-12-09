// Copyright 2021 Chuwei Chen chenchuw@bu.edu

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int twice(int &x) {
    x = 1+x;
    return 2*x;
}

int main(int argc, char **argv) {
  int x = 2;
  int b= twice(x);
  cout << x << endl;

  cout << "===" << endl;

  int a[5];
  char *c[5];

  

  cout << c << endl;

  cout << "===" << endl;

  for (int i=0; i<5; i++){
    a[i] = i;
  }

  for (int i=0; i<5; i++) {
    cout << a[i] << endl;
  }

  cout << "===" << endl;

  cout << *(a+2) << " same as " << a[2] << endl;

  cout << a << " a+1 becomes: " << a+1 << endl;

  cout << "so one increment of an array in the address is 4" << endl;

}
