#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> v) {
    
    int size = v.size();
    cout << "printing vector: " << endl;
    for (int i = 0; i < size; i++) {
        cout << v.at(i) << " ";
    }
    cout << endl;
}

int main() {
    //how to copy vector
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> arr1(arr);  //copying vector arr to arr1
    arr1.pop_back();  //removing the last element from arr1
    arr.push_back(50);  //adding element 50 to the end of arr
    
    print(arr1);
    print(arr);

    return 0;
}