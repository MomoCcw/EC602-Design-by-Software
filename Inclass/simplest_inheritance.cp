// Copyright 2021 J.Carruthers jbc@bu.edu

class Base {
 public:
  int x;
};

class Derived : public Base { };

int main() {
  Derived d;
  d.x = 0;
}
