// Copyright 2021 Chuwei Chen chenchuw@bu.edu
// Copyright 2021 Zhaozhong Qi zqi5@bu.edu

#include<cstdint>
#include<iostream>

using std::cout;

int main() {
  int64_t num_in;

  while (true) {
    int64_t sum = 0;
    std::cin >> num_in;
    if (2 <= num_in && num_in <= 2147483647) {
      cout << num_in << ": 1";
      for (int i = 1; i <= num_in / 2; i++) {
        if (num_in % i == 0) {
          sum += i;
          if (i != 1)
            cout << "+" << i;
        }
      }
      cout << " = " << sum << "\n";
    } else if (num_in == 0) {
      return 0;
    } else {
      cout << "Try again! Please pick between 2 and 2147483647.\n";
    }
  }
}
