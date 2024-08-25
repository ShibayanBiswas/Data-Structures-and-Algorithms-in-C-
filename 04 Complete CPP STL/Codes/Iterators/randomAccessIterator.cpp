#include <iostream>
#include <vector>
using namespace std;

// Random Access Iterator
int main() {
    
    vector<int> arr;
    arr.push_back(10);
    arr.push_back(20);
    arr.push_back(30);
    arr.push_back(40);
    arr.push_back(50);

    // Forward traversal with modification
    vector<int>::iterator it = arr.begin();
    while (it != arr.end()) {
        // Write operation: increment each element by 7
        *it = *it + 7;
        // Read operation: print the modified value
        cout << *it << " ";
        // Move forward
        it++;
    }
    cout << endl;

    // Backward traversal
    vector<int>::iterator itb = arr.end();
    while (itb != arr.begin()) {
        // Move backward
        itb--;
        // Read and print the value
        cout << *itb << " ";
    }
    cout << endl;

    // Random access: Accessing the 4th element (index 3)
    vector<int>::iterator itr = arr.begin() + 3;
    cout << "Random access element (4th element): " << *itr << endl;

    return 0;
}