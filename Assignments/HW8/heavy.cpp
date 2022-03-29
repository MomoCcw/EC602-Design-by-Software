// Copyright 2021 Chuwei Chen chenchuw@bu.edu
// Copyright 2021 Zhaozhong Qi zqi5@bu.edu

#include <string>
#include <vector>

using std::string;
using std::vector;
using std::stoi;

string convertbase(int num, int tobase) {
  // Convert num from base 10 to base 'tobase'
  if (num == 0)
    return "0";
  int remainder;
  string newbase_num;
  while (num > 0) {
    remainder = num % tobase;
    num = num / tobase;
    newbase_num = static_cast<char>(remainder + '0') + newbase_num;
  }
  return newbase_num;
}

int heavy(int num, int base) {
  // Return 1 if num is heavy number in base 'base', otherwise return 0.
  string converted_num = convertbase(num, base);
  vector<string> sum_track;
  while (true) {
    int sqr_sum = 0;
    for (int i = 0; i < converted_num.length(); i++) {
      sqr_sum += (converted_num.at(i) - '0') * (converted_num.at(i) - '0');
    }
    converted_num = convertbase(sqr_sum, base);

    // Found heavy number! Return 1!
    if (converted_num == "1")
      return 1;

    // Search converted_num in the track list, if exist return 0
    for (int i = 0; i < sum_track.size(); i++) {
      if (converted_num == sum_track.at(i))
        return 0;
    }

    // else add converted_num to the list
    sum_track.push_back(converted_num);
  }
  return 0;
}

int main(int argc, char **argv) {
  return heavy(stoi(argv[1]), stoi(argv[2]));
}
