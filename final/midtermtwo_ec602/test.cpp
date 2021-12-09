#include<iostream>
#include<string>
#include<vector>
using std::string;
using std::vector;
using namespace std;

// Any base to base 10
string convertbase(string numstr, int frombase) {
  int base10_num = 0, power = 1;

  // 1. convert string from whatever base to base 10
  for (int i = numstr.size() - 1; i >= 0; i--) {
    base10_num += (numstr.at(i) - '0') * power;
    power = power * frombase;
  }

  return to_string(base10_num);
}

// Base 10 to any base
string convertbase2(int base10_num, int tobase) {
  bool neg = false;
  if (base10_num == 0)
    return "0";
  if (base10_num < 0) {
    neg = true;
    base10_num = base10_num*(-1);
  }

  string newbase_num;
  int remainder;
  while (base10_num > 0) {
    remainder = base10_num % tobase;
    base10_num = base10_num / tobase;
    newbase_num = static_cast<char>(remainder + '0') + newbase_num;
  }
  if (neg)
    newbase_num = '-' + newbase_num;
  return newbase_num;
}

class SumParser {
  public:
    string _s;
    int _base;

    SumParser(string s, int base) {
      // TODO: base invalid

      _s = s;
      _base = base;
    }

    int get_value() {
      // abcd & base invalid
      for (int i=0; i<_s.length(); i++) {
        if (!isdigit(_s[i]) and _s[i]!='+' and _s[i]!='-')
          throw(0);
        if (isdigit(_s[i])) {
          if (_s[i]-'0' >= _base)
            throw(0);
        }
      }

      vector<string> numList;
      vector<char> operatorList;

      int pos = 0;
      for (int i=0; i<_s.length(); i++) {
        if (_s[i] == '+' or _s[i] == '-') {
          char _operator = _s[i];
          operatorList.push_back(_operator);
          string buffer = _s.substr(pos,i-pos);

          for (int i=0; i<buffer.length(); i++) {
            if (buffer[i] == '+' or buffer[i] == '-') {
              buffer.erase(i,1);
            }
          }

          numList.push_back(convertbase(buffer,_base));
          pos = i;
        }
      }

      string buffer2 = _s.substr(pos);
      for (int i=0; i<buffer2.length(); i++) {
        if (buffer2[i] == '+' or buffer2[i] == '-') {
          buffer2.erase(i,1);
        }
      }
      numList.push_back(convertbase(buffer2,_base));

      int pointer = 0;
      int acc = stoi(numList[0]);
      for (int i=0; i<operatorList.size(); i++) {
        if (operatorList[i]=='+') {
          acc = acc + stoi(numList[i+1]);
          pointer++;
        } else {
          acc = acc - stoi(numList[i+1]);
          pointer++;
        }
      }
      return acc;
    }

    string show_result() {
      // Just convert get_value result to the specified base
      int ans = get_value();
      return convertbase2(ans,_base);
    }
};



int main() {
  std::string s;
  int base;
  while (std::cin >> base >> s) {
    SumParser a{s, base};
    try {
      std::cout << a.get_value() << " "
                << a.show_result() << "\n";
    } catch (...) {
      std::cout << "invalid\n";
    }
  }

  // test code for vistance
  // this is very bare-bones, you will want to do more testing

  //return vistance({3, 6, 9}, {9, 3, 6});
  return 0;
}