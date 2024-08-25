#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    
    vector<int> first;
    first.push_back(1);
    first.push_back(2);
    first.push_back(3);
    first.push_back(4);

    vector<int> second;
    second.push_back(3);
    second.push_back(4);
    second.push_back(5);
    second.push_back(6);

    // Set Union
    vector<int> result;
    set_union(first.begin(), first.end(), second.begin(), second.end(), inserter(result, result.begin()));
    cout << "Union: ";
    for (int a : result) {
        cout << a << " "; 
    }
    cout << endl;

    // Set Intersection
    vector<int> result2;
    set_intersection(first.begin(), first.end(), second.begin(), second.end(), inserter(result2, result2.begin()));
    cout << "Intersection: ";
    for (int a : result2) {
        cout << a << " "; 
    }
    cout << endl;

    // Set Difference (elements in `first` but not in `second`)
    vector<int> result3;
    set_difference(first.begin(), first.end(), second.begin(), second.end(), inserter(result3, result3.begin()));
    cout << "Difference (first - second): ";
    for (int a : result3) {
        cout << a << " "; 
    }
    cout << endl;

    // Set Symmetric Difference (elements in either `first` or `second`, but not both)
    vector<int> result4;
    set_symmetric_difference(first.begin(), first.end(), second.begin(), second.end(), inserter(result4, result4.begin()));
    cout << "Symmetric Difference: ";
    for (int a : result4) {
        cout << a << " "; 
    }
    cout << endl;

    return 0;
}