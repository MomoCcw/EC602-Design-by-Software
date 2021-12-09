#include "ec602.hpp"
using namespace ec602;
int main(int argc,char** argv) {
  
  // char** argv (stores addresses of input char*) 
  // -> char* (store addresses)
  // -> char (the character, like a, r, g)

  for (int i=0; i < argc; i++){
    cout << i << " *(argv+i) " << *(argv+1) << " argv[i] " << argv[i] 
    << " argv+i " << argv+i << "\n";
  }

  // for (int i=0; i<argc; i++) {
  //   int j=0;
  //   while (argv[i][j] != '\0') {
  //     cout << argv[i][j];
  //     j++;
  //   }
  //   cout << "\n";
  // }

  // string s;
  // for (int i=0; i<argc; i++) {
  //   s = argv[i];
  //   cout << s << " " << s.size() << "\n";
  // }
}