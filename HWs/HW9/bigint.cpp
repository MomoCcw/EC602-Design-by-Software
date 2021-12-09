// Copyright 2021 Chuwei Chen chenchuw@bu.edu
// Copyright 2021 Zhaozhong Qi zqi5@bu.edu

#include <string>
#include <vector>
#include "bigint.h"

using std::string;
using std::to_string;
using std::vector;

string findSum(string str1, string str2) {
  // Make sure str2 is longer
  if (str1.length() > str2.length()) {
    string temp = str2;
    str2 = str1;
    str1 = temp;
  }

  string ans;
  int carry = 0, n1 = str1.length(), n2 = str2.length();

  // Compute sum of each digit
  for (int i = str1.length() - 1; i >= 0; i--) {
    int sum = ((str1.at(i) - '0') + (str2.at(i + n2 - n1) - '0') + carry);
    char digit = (sum % 10 + '0');
    ans = digit + ans;
    carry = sum / 10;
  }

  // Add remaining digits of longer string
  for (int i = n2 - n1 - 1; i >= 0; i--) {
    int sum = ((str2.at(i) - '0') + carry);
    char digit = (sum % 10 + '0');
    ans = digit + ans;
    carry = sum / 10;
  }

  // Add remaining carry
  if (carry) {
    char digit = (carry + '0');
    ans = digit + ans;
  }
  return ans;
}

BigInt multiply_int(const BigInt &a, const BigInt &b) {
  // if multiply by 0, return 0.
  if (a == "0" || b == "0")
    return "0";

  string short_input = a;
  string long_input = b;

  if (a.size() > b.size()) {
    long_input = a;
    short_input = b;
  }

  // Multiply part
  vector<string> sum_list;
  for (int i = short_input.length() - 1; i >= 0; i--) {
    int carry = 0;
    int product = 0;
    string buffer;
    int b_digit = short_input.at(i) - '0';

    for (int j = long_input.length() - 1; j >= 0; j--) {
      int a_digit = long_input.at(j) - '0';
      product = b_digit * a_digit + carry;
      int digit = product % 10;

      if (j == 0 && product > 9) {
        digit = product;
        char a = digit % 10 + '0';
        char b = digit / 10 + '0';
        buffer = a + buffer;
        buffer = b + buffer;
      } else {
        char a = digit + '0';
        buffer = a + buffer;
      }
      carry = product / 10;
    }
    sum_list.push_back(buffer);
  }

  // Sum part
  int64_t sum = 0;
  string sum_str = sum_list.at(0);

  for (int i = 0; i < sum_list.size() - 1; i++) {
    if (sum_list.at(i).size() == 1)
      sum_list.at(i) = "0" + sum_list.at(i);
    string add = sum_str.substr(0, sum_str.size() - (i + 1));
    string hanger;

    hanger = sum_str.substr(sum_str.size() - (i + 1), sum_str.size());

    if (!add.empty())
      sum_str = findSum(add, sum_list.at(i + 1));

    sum_str = sum_str + hanger;
  }
  return sum_str;
}

#include <iostream>
using namespace std;
int main() {
  string ans = multiply_int("24983498348958982398747892348972358972398723789489723789478912389712983549898983483493498934", "123438945342589723478952347895789234678923456987234897523489752348975789234578932489752389745789234897578923452345645363457346734673468935983");
  std::cout << ans << endl << "Length is: " << ans.size() << endl;
}

