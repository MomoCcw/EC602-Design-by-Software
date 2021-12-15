// Class variables
//   static

// Inheritance
//    public > protected > private

//Access					 public	protected         private
//
//members of the same class	 yes		yes			   yes
//members of derived class	 yes		yes			   no
//not members		           yes		no			   no

// if the inheritance type is protected or private, then everything
// inherited gets "promoted" to this more restrictive access type.

// class A : ITYPE B
// B is the base class
// A is the derived class

// A is a B and all members of B are at least ITYPE.


// LEGEND: 
//  @ public  ?protected   !private   <reuses from before  NA not available
//
//  Animal  -public->   Bird  --prot->   Chicken  --priv->  Delaware   -public->    ExtraLargeDelaware
//  
//  @count              < @count      ?   < ?count     !    < !count     EOL
//                                        @count()     !    @count()               <@count          
//  @is_wild            < @is_wild    ?   @is_wild     !    @is_wild               <@is_wild   
//  @is_alive           < @is_alive   ?   @is_alive    !    @is_alive              <@is_alive 
//  ?wild               < ?wild           < ?wild      !    < !wild      EOL      
//  ?alive              < ?alive          < ?alive     !    < !alive     EOL     
//                      @escape       ?   < ?escape    !    < !escape
//                                        @go_free     !    @go_free
//                      @ground       ?   < ?ground
//                      @can_fly      ?   @can_fly     !    @can_fly              <@can_fly
//                      !has_wings   EOL     
//                                        !clucks     EOL  
//                                                          !is_cute

#include <iostream>
using std::cout;
using std::endl;

class Animal {
 public:
  Animal();

  static int count; // there is only one of these ever.

  bool is_wild () { return wild; }
  bool is_alive () { return alive;}

 protected:
  bool wild;
  bool alive;
};

int Animal::count = 0;

Animal::Animal() {
  alive = true;
  wild = true;
  count++;
}

class Bird : public Animal {
 public:
  Bird() {  has_wings = true;}

  void ground()  { has_wings = false; }
  void escape()  { wild = true; }
  bool can_fly() { return has_wings; }
 private:
  bool has_wings;
};


class Chicken: protected Bird {  
// Animal: count, is_wild, is_alive are now protected
// Bird:   escape, can_fly now protected
 public:
  Chicken() { wild = false;}

  bool is_wild()  { return wild; }
  bool is_alive() { return Bird::is_alive(); }
  int count()     {  return Animal::count; }

  bool can_fly()  { return false; }
  void go_free()  { escape(); }

 private:
  bool clucks;
};


class Delaware: private Chicken { 
// count, is_wild and is_alive are now off-limits to Delaware's
 private:  bool cute;
 
 public:
  Delaware()      { cute = true;}
  bool is_wild()  { return wild;}
  bool is_alive() { return alive; }
  bool can_fly()  { return false; }
  int count()     { return Animal::count; }
  bool is_cute()  { return cute; }
  void go_free()  { //escape(); 
    Chicken::go_free(); 
    //Bird::escape();
}


  // not allowed
  // bool make_sound() {return clucks;}

} ;

class ExtraLargeDelaware : public Delaware {
 public:
  //not allowed
  // bool check_wild() {return wild;}
} ;



int main() {
  //Animal::count=100;

  Animal a;
  //a.wild;
  cout << "a: w a " << a.is_wild() << " " << a.is_alive()
       << ", # " << a.count << " " << Animal::count << endl;

  Bird b;
  // b.wild;
  // b.has_wings;
  cout << "b: w a " << b.is_wild() << " " << b.is_alive()
       << ",f "     << b.can_fly()
       << ", # "    << b.count << " " << Animal::count << endl;

  Chicken c;
  c.go_free();
  // c.escape();
  cout << "c: w a " << c.is_wild() << " " << c.is_alive()
       << ",f "     << c.can_fly()
       << ", # "    << c.count() << " " << Animal::count << endl;

  Delaware d;
  d.go_free();
  cout << "d: w a " << d.is_wild() << " " << d.is_alive()
       << ",f "     << d.can_fly()
       << ", # "    << d.count() << " " << Animal::count << " " << (d.is_cute() ? "cute" : "ugh") << endl;

  ExtraLargeDelaware e;
  cout << "e: w a " << e.is_wild() << " " << e.is_alive()
       << ",f "     << e.can_fly()
       << ", # "    << e.count() << " " << Animal::count << " " << (e.is_cute() ? "cute" : "ugh") << endl;

}