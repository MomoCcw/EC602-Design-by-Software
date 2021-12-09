
#include "ec602.hpp"
using namespace ec602;

// the interface (could go in a .h/.hpp file)
class Complex {
 private:
    double _r, _i;
 public:
    Complex();
    Complex(double,double);

    double abs();
    double real();
    double imag();

    friend istream& operator>>(istream& in_st,Complex& z) {
        in_st >> z._r >> z._i;
        return in_st;
    }

    friend ostream& operator<<(ostream& out_st,Complex& z) {
        out_st << "<" << z._r << "," << z._i << ">";
        return out_st;
    }
};

// the implementation

// default constructor. python:: __init__
Complex::Complex() {
    _r = _i = 0;
}

Complex::Complex(double x, double y) {
    _r = x;
    _i = y;
}

double Complex::abs() {
 return sqrt(_r*_r  + _i*_i);
}

int main(int argc, char** argv) {
 
 Complex c(3,4);
 
 cout << c.abs() << "\n";

  cin >> c;
  cout << c << "\n";

}