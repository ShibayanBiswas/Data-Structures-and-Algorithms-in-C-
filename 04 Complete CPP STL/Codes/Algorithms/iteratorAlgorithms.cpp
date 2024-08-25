#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Function to print double of the given number
void printDouble(int a) {

    cout << 2 * a << " ";
}

// Function to check if the given number is even
bool checkEven(int a) {
    
    return a % 2 == 0;
}

int main() {

    vector<int> arr(6);
    arr[0] = 11;
    arr[1] = 11;
    arr[2] = 21;
    arr[3] = 40;
    arr[4] = 50;
    arr[5] = 60;

    // unique: Remove consecutive duplicate elements
    auto it = unique(arr.begin(), arr.end()); // returns iterator to the new end of the range
    arr.erase(it, arr.end()); // erase the duplicate elements beyond the unique range
    cout << "Array after unique operation: ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    // rotate: Rotate elements to the left by 3 positions
    rotate(arr.begin(), arr.begin() + 3, arr.end());
    cout << "Array after rotation: ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    // for_each: Apply the printDouble function to each element
    cout << "Doubles of array elements: ";
    for_each(arr.begin(), arr.end(), printDouble);
    cout << endl;

    // find: Find the first occurrence of the target element
    int target = 40;
    auto it1 = find(arr.begin(), arr.end(), target); // returns iterator
    cout << "Found target element: " << *it1 << endl;

    // find_if: Find the first element that satisfies the checkEven condition
    auto it2 = find_if(arr.begin(), arr.end(), checkEven); // returns iterator
    cout << "First even element found: " << *it2 << endl;

    // count: Count occurrences of the target element
    int targetc = 11;
    int ans = count(arr.begin(), arr.end(), targetc);
    cout << "Count of target element " << targetc << ": " << ans << endl;

    // count_if: Count elements that satisfy the checkEven condition
    int ans2 = count_if(arr.begin(), arr.end(), checkEven);
    cout << "Count of even elements: " << ans2 << endl;

    // sort: Sort the array
    sort(arr.begin(), arr.end());
    cout << "Array after sorting: ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    // reverse: Reverse the array
    reverse(arr.begin(), arr.end());
    cout << "Array after reversing: ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    // partition: Partition the array such that even elements are on the left
    partition(arr.begin(), arr.end(), checkEven);
    cout << "Array after partitioning (even elements on the left): ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    return 0;
}