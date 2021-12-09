#include<iostream>
#include<string>
#include<vector>
using std::string;
using std::vector;
using namespace std;

vector<int> num_map(vector<string> data_in) {
    vector<int> map_in;
    for (int i = 0; i < data_in.size; i++) {
        map_in.at(data_in.at(i)) = i;
    }
    return map_in;
}

int cal_dis(vector<string> in1, vector<string> in2) {
    int dis = 0;
    if (in1.size() != in2.size()) {
        return -1;
    }
    vector<int> map1 = num_map(in1);
    vector<int> map2 = num_map(in2);
    for (int i = 0; i < in1.size(); i++) {
        if (map2.at(in1.at(i ))) {
            if (map1.at(in1.at(i)) - map2.at(in1.at(i)) >= 0) {
                dis += map1.at(in1.at(i)) - map2.at(in1.at(i));
            }
            else {
                dis += map2.at(in1.at(i)) - map1.at(in1.at(i));
            }
        }
        else {
            return -1;
        }
    }
    return dis;
}
// template for vistance

int vistance(const vector<int> &a, const vector<int> &b) {
    if (cal_dis(a, b) > 0) {
        cout << cal_dis（a, b）
        return cal_dis(a, b);
    }
    else {
        cout << "vistance is an illusion";
        return ; // placeholder return, change it to correct value
    }
}

int main() {
    vistance([])
}