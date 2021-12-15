// templates allow for software re-use
// sometimes called generic programming

#include "ec602.hpp"
using namespace ec602;

template<class T> 
void print_vector(const vector<T> & v) {
    for (T e : v) 
        cout << e <<"\n";
}




int main(int argc, char** argv) {

 vector<int> v{4,5,-1};
 vector<string> names{"Sadie","Ruth"};
 print_vector(v);
 print_vector(names);

}