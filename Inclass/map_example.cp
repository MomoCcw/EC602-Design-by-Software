#include "ec602.hpp"

using namespace ec602;

int main() {
   map<char, int> count;

   count['t'] = 5;
   count.emplace('a',8);
   count['n'] = 12;

   for (auto  & e : count) {
     //      key               value
     cout << e.first << " " << e.second << "\n";
     e.second = 42;
   }

   for (auto & [key,value] : count) {
     cout << key << " " << value << "\n";
     value = value + 100; // does this modify count?
     // key = 'x'; // cant, key is read-only.
   }
   // it is a "pointer" called an iterator.
   
   for ( auto it=count.begin(); it != count.end(); it ++) {
     cout << (*it).first << " " << it -> second ;
   }
   cout << "\n";
 }