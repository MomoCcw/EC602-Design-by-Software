#include <iostream>
#include <vector>
#include "bigint.h"

int main() {
  BigInt A, B;

  std::cin >> A >> B;

  std::cout << multiply_int(A, B) << std::endl;
}
