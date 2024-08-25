#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    
    vector<int> arr;

    // Insert elements into the vector
    arr.push_back(22);
    arr.push_back(11);
    arr.push_back(55);
    arr.push_back(66);
    arr.push_back(77);

    // Convert the vector into a heap
    make_heap(arr.begin(), arr.end()); 
    // Print the heap
    cout << "After make_heap: ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    // Insertion: Add a new element and push it into the heap
    arr.push_back(99);
    push_heap(arr.begin(), arr.end()); 
    // Print the heap after insertion
    cout << "After push_heap (insertion of 99): ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    // Deletion: Pop the largest element from the heap
    pop_heap(arr.begin(), arr.end()); 
    // Remove the popped element from the vector
    arr.pop_back();
    // Print the heap after deletion
    cout << "After pop_heap (deletion of largest element): ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    // Sort the heap (convert it into a sorted array)
    sort_heap(arr.begin(), arr.end()); 
    // Print the sorted array
    cout << "After sort_heap: ";
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    return 0;
}