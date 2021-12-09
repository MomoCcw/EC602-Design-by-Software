#include <iostream>
#include "ec602.hpp"

using std::cin;
using std::cout;

int sum_range(int a, int b) {
	int iterator = a;
	int sum = 0;

	while (iterator <= b) {
		sum = sum + iterator;
		iterator += 1;
	}
	return sum;
}

void print_fancy(int a, int b) {
	for (int i=a; i <= a+2; i++) {
		cout << i << '+';
	}
	cout << "...";
	for (int i=b-2; i <= b; i++) {
		cout << "+" << i;
	}
	cout << '=' << sum_range(a,b) << "\n";
}

void print_normal(int a, int b) {
	int i = a;
	while (i < b) {
		cout << i++ << '+';
	}
	cout << b << '=' << sum_range(a,b) << "\n";
}

int main() {
	int a,b;
	cout << "Enter two integers: " << '\n';
	cin >> a >> b;
	if (b-a > 6)
		print_fancy(a,b);
	else
		print_normal(a,b);

}