#include <iostream>
#include <vector>
using namespace std;

int main() {
    
    vector<int> arr;
    arr.push_back(10);
    arr.push_back(20);
    arr.push_back(30);

    // Traverse using iterator
    vector<int>::iterator it = arr.begin();
    while (it != arr.end()) {
        cout << *it << " "; // Dereference iterator to access element
        it++; // Move iterator to the next element
    }
    cout << endl;

    return 0;
}