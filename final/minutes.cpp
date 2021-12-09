// Copyright 2021 Chuwei Chen chenchuw@bu.edu

#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::string;
using std::to_string;
using std::vector;

// PART 1 ANSWER
string get_minute(int time) {
	// Label out of range
	if (time > 1439 or time < 0) {
		throw(0);
	}

	int hour, minute;
	string ans;
	// Compute hour and minute, 60min/hr
	hour = time / 60;
	minute = time % 60;

	string hour_str = to_string(hour);
	string minute_str = to_string(minute);

	if (hour_str.length() == 1) {
		hour_str = "0" + hour_str;
	}

	if (minute_str.length() == 1) {
		minute_str = "0" + minute_str;
	}

	ans = hour_str + ":" + minute_str;

	return ans;
}

// PART 2 ANSWER
class Minute {
public:
	int label;
	bool enable_exception;
	// CONSTRUCTOR
	Minute(int label_in, bool exceptEnable_in) {
		// Label out of range
		if ((label_in < 0 or label_in > 1439) and exceptEnable_in == true) {
			throw(0);
		}
		label = label_in;
		enable_exception = exceptEnable_in;
	}

	vector<string> all_minutes() {
		vector<string> ans;
		for (int i=0; i<1440; i++) {
			// Instead of .push_back, using .insert
			ans.insert(ans.end(),::get_minute(i));
		}
		return ans;
	}

	string get_minute() {
		int hour, minute;
		string ans;
		hour = label / 60;
		minute = label % 60;

		string hour_str = to_string(hour);
		string minute_str = to_string(minute);

		if (hour_str.length() == 1) {
			hour_str = "0" + hour_str;
		}

		if (minute_str.length() == 1) {
			minute_str = "0" + minute_str;
		}

		if (label < 0 or label > 1439 and enable_exception == false) {
			ans = "??:??";
		} else {
			ans = hour_str + ":" + minute_str;
		}

		return ans;
	}
};


int main() {
	// PART 3 ANSWER

	// PART 1 TEST CODE
	cout << "=====PART 1 test=====" << endl;
	cout << "PART1 test1 (label=1439): \n" << get_minute(1439) << endl;
	cout << "PART1 test2 (label=89): \n" << get_minute(89) << endl;
	try {
		cout << get_minute(1440) << endl;
	} catch (...) {
		cout << "PART1 OUT OF RANGE (label=1440)" << endl;
	}
	try {
		cout << get_minute(-1) << endl;
	} catch (...) {
		cout << "PART1 OUT OF RANGE (label=-1)" << endl;
	}

	// PART 2 TEST CODE
	cout << "=====PART 2 test=====" << endl;
	Minute obj(1439, true);
	cout << "PART2 CONSTRUCTOR TEST 1 PASSED" << endl;

	try {
		Minute obj(1440, true);
	} catch (...) {
		cout << "PART2 CONSTRUCTOR TEST 2 OUT OF RANGE WHEN CONSTRUCTING \
(label=1440, enable_exception=true)" << endl;
	}

	try {
		Minute obj(-1, true);
	} catch (...) {
		cout << "PART2 CONSTRUCTOR TEST 3 OUT OF RANGE WHEN CONSTRUCTING \
(label=-1, enable_exception=true)" << endl;
	}

	cout << "PART2 test4 get_minute TEST (label=1439, enable_exception=true):\
\n" << obj.get_minute() << endl;

	Minute obj2(89, true);
	cout << "PART2 test5 get_minute TEST (label=89, enable_exception=true):\
\n" << obj2.get_minute() << endl;

	Minute obj3(-1, false);
	cout << "PART2 test6 get_minute TEST (label=-1, enable_exception=false):\
\n" << obj3.get_minute() << endl;

	Minute obj4(1440, false);
	cout << "PART2 test7 get_minute TEST (label=1440, enable_exception=false):\
\n" << obj4.get_minute() << endl;

	vector<string> allMinutes = obj.all_minutes();
	cout << "PART2 test8 all_minutes TEST:" << endl;
	for (auto e:allMinutes)
		cout << e << endl;
	cout << "Length of vector returned from all_minutes(): " \
	     << allMinutes.size() << endl;

	cout << "=====PART3 TESTING FINISHED=====" << endl;
}
