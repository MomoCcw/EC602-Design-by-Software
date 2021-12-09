#include <iostream>
#include "ec602.hpp"

using namespace std;

int main() {
	int a,b;
	cout << "Enter two integers: " << '\n';
	cin >> a >> b;

	int iterator = a;
	int sum = 0;
	while (iterator <= b) {
		cout << iterator << (iterator==b ? '=' : '+');
		sum = sum + iterator;
		iterator += 1;
	}
	cout << sum << "\n";
}