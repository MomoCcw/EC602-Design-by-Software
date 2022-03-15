// Midterm Two: C++
// Solution

#include<string>
#include<vector>
#include<iostream>
using std::string;
using std::vector;
using std::cout;
using std::to_string;

const int MINPERDAY = 1440;
const int MINPERHR = 60;

namespace my {
string get_minute(int label, bool exceptions = true) {
  string minute, hour;
  if (label<0 or label >= MINPERDAY) {
    if (exceptions)
      throw "bad label";
    return "??:??";
  }

  minute = to_string(label % MINPERHR);
  hour = to_string(label / MINPERHR);

  if (minute.size() == 1) minute = "0" + minute;
  if (hour.size() == 1) hour = "0" + hour;
  return hour + ":" + minute;
}

}

class Minute {
  bool exceptions;
 public:
  Minute(bool enable_exception = true) {
    exceptions = enable_exception;
  }
  string get_minute(int i) {
    return my::get_minute(i, exceptions);
  }
  vector<string> all_minutes() {
    vector<string> m(MINPERDAY);
    for (int i = 0; i < MINPERDAY; i++)
      m.at(i) = get_minute(i);
    return m;
  }
} ;

int main() {
  // this is not the best example of a test suite.
  
  cout << my::get_minute(1439) << "\n";

  Minute m;
  cout << m.get_minute(45) << "\n";
  vector<string> v = m.all_minutes();
  cout << v.at(1234) << "\n";

  Minute t(false);
  cout << t.get_minute(-1) << "\n";
}

