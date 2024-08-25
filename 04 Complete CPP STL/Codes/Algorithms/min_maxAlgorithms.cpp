#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    
    int a = 10;
    int b = 15;

    // min: Find the minimum of two numbers
    cout << "Minimum of " << a << " and " << b << " is: " << min(a, b) << endl;

    // max: Find the maximum of two numbers
    cout << "Maximum of " << a << " and " << b << " is: " << max(a, b) << endl;

    vector<int> arr;
    arr.push_back(10);
    arr.push_back(20);
    arr.push_back(30);
    arr.push_back(40);
    arr.push_back(50);

    // min_element: Find the minimum element in the vector
    auto it = min_element(arr.begin(), arr.end());
    cout << "Minimum element in the array is: " << *it << endl;

    // max_element: Find the maximum element in the vector
    auto it1 = max_element(arr.begin(), arr.end());
    cout << "Maximum element in the array is: " << *it1 << endl;

    return 0;
}