// Copyright 2021 Chuwei Chen chenchuw@bu.edu
// Copyright 2021 Zhaozhong Qi zqi5@bu.edu

#include <iostream>
#include <map>
#include <string>
#include <vector>
#include "movedef.h"

char tttresult(std::string board) {
  int x_count = 0, y_count = 0;
  for (int i = 0; i < board.size(); ++i) {
    if (board.at(i) != 'x' && board.at(i) != '#'
        && board.at(i) != 'o' || board.size() != 9)
      return 'e';
    if (board.at(i) == 'x') x_count++;
    if (board.at(i) == 'o') y_count++;
  }
  if (x_count - y_count > 1 || y_count > x_count) return 'i';
  std::map<char, int> m = {{'x', 0}, {'o', 0}, {'#', 0}};
  for (int j = 0; j <= 6; j = j + 3)
    if (board.at(j) == board.at(j + 1) && board.at(j) == board.at(j + 2))
      m.at(board.at(j)) += 1;
  for (int k = 0; k < 3; k++)
    if (board.at(k) == board.at(k + 3) && board.at(k) == board.at(k + 6))
      m.at(board.at(k)) += 1;
  if (board.at(0) == board.at(4) && board.at(4) == board.at(8))
    m.at(board.at(0)) += 1;
  if (board.at(2) == board.at(4) && board.at(4) == board.at(6))
    m.at(board.at(2)) += 1;
  if ((m.at('x') == 1 && x_count == y_count)
      || (m.at('o') == 1 && x_count != y_count))
    return 'i';
  if (m.at('x') >= 1) return 'x';
  if (m.at('o') >= 1) return 'o';
  if (x_count + y_count == 9) return 't';
  return 'c';
}

char tttresult(std::vector<Move> board) {
  std::string s = "#########";
  for (int i = 0; i < board.size(); i++) {
    int index = board.at(i).r * 3 + board.at(i).c;
    // Row, Col size check && Player char check
    if (board.at(i).r > 2 || board.at(i).c > 2 ||
        board.at(i).player != 'x' && board.at(i).player != 'o')
      return 'e';
    s.at(index) = board.at(i).player;
    // First player char check, consecutive players cannot be the same check
    if (i != board.size() - 1 &&
        s.at(index) == board.at(i + 1).player || board.at(0).player != 'x')
      return 'i';
  }
  return tttresult(s);
}

std::string dec2ter(int base_ten) {
  std::string result = "";
  while (base_ten > 0) {
    result = static_cast<char>(('0' + base_ten % 3)) + result;
    base_ten /= 3;
  }
  while (result.size() < 9)
    result = '0' + result;
  return result;
}

std::vector<std::string> get_all_boards() {
  std::vector<std::string> all_boards;
  for (int i = 0; i < 19683; i++) {
    std::string s = "";
    for (int j = 0; j < 9; j++) {
      if (dec2ter(i).at(j) == '0') s += 'x';
      if (dec2ter(i).at(j) == '1') s += 'o';
      if (dec2ter(i).at(j) == '2') s += '#';
    }
    all_boards.push_back(s);
  }
  return all_boards;
}


void ttt_tally() {
  std::vector<std::string> all_boards = get_all_boards();
  std::map<char, int> tally =
  {{'x', 0}, {'o', 0}, {'t', 0}, {'i', 0}, {'c', 0}};
  for (int i = 0; i < all_boards.size(); i++)
    tally.at(tttresult(all_boards.at(i))) += 1;
  std::cout << "x " << tally.at('x') << "\n" << "o " << tally.at('o') << "\n"
            << "t " << tally.at('t') << "\n" << "i " << tally.at('i')
            << "\n" << "c " << tally.at('c') << "\n";
}


// MAIN

int main() {
  int n;
  std::string board;
  Move m;
  std::vector<Move> moves;
  std::vector<std::string> boards;
  std::string asktype;

  while (std::cin >> asktype) {
    if (asktype == "v") {  // test tttresult vector
      moves.clear();
      std::cin >> n;
      for (int i = 0; i < n; i++) {
        std::cin >> m.r >> m.c >> m.player;
        moves.push_back(m);
      }
      std::cout << tttresult(moves) << "\n";
    } else if (asktype == "s") {  // test tttresult string
      std::cin >> board;
      std::cout << tttresult(board) << "\n";
    } else if (asktype == "a") {  // test get_all_boards
      boards = get_all_boards();
      for (auto b : boards) {
        std::cout << b << "\n";
      }
    } else if (asktype == "t") {  // test ttt_tally
      ttt_tally();
    } else {
      return 0;
    }
  }
  return 0;
}
