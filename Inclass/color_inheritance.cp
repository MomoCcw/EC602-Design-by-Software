// Copyright 2021 EC602/J Carruthers jbc@bu.edu

// Inheritance: derived and base classes
//               Cat          Animal
//              morespecific  moregeneral
//               subclass    superclass
//       DONT:     child        parent

//
// class is the same as struct
// EXCEPT members are private instead of public
//

#include <string>
#include <iostream>
using std::cout;
using std::string;

// Example: Derived is-a Base
class AnotherBase{ 
protected:
 int y;
};

class MoreDerived : public AnotherBase {
  public:

  MoreDerived() {
    y = 1;
  }
  int get_value() {
    return y;
  }
} ;

struct Base {
  int x;
};

struct Derived : Base { 

};



// NamedColor is-a Color
struct Color {
    int red,green,blue;
    Color(){ red = green = blue =0; }
    double brightness();
} ;

double Color::brightness() {
        return (red + green + blue)/3.0;
}


struct NamedColor : Color {
    string name; // part of the object
    NamedColor(string name) {
        // name is a parameter, from line 57
        // this->name is the var on line 56.
        this->name = name;
    }


} ;

int main(){
  NamedColor lb{"lightblue"};

  // blue and brightness are inherited from Color
  lb.blue=25;
  cout << lb.brightness() << "\n";
 
  // x is inherited from Base
  Derived d;
  d.x = 0;

  MoreDerived m;
  cout << m.get_value() << "\n";
  //m.y = 2;
}

