// Copyright 2021 Chuwei Chen chenchuw@bu.edu
// Copyright 2021 Zhaozhong Qi zqi5@bu.edu

#include<iostream>
#include<string>

using std::cin;
using std::cout;
using std::string;
using std::stoi;

string convertbase(string numstr, int frombase, int tobase) {
  int base10_num = 0, power = 1;
  // 1. convert string from whatever base to base 10
  for (int i = numstr.size() - 1; i >= 0; i--) {
    base10_num += (numstr.at(i) - '0') * power;
    power = power * frombase;
  }

  // 2. convert base10_num to digit_newbase
  string newbase_num;
  int remainder;
  while (base10_num > 0) {
    remainder = base10_num % tobase;
    base10_num = base10_num / tobase;
    newbase_num = static_cast<char>(remainder + '0') + newbase_num;
  }
  return newbase_num;
}

int main(int argc, char** argv) {
  // Three command line arguments: number, frombase, tobase.
  cout << convertbase(argv[1], stoi(argv[2]), stoi(argv[3])) << "\n";
  return 0;
}

