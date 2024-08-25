#include <iostream>
#include <vector>
#include <list>
using namespace std;

// Bidirectional Iterator
int main() {
    
    list<int> myList;
    myList.push_back(10);
    myList.push_back(20);
    myList.push_back(30);

    // Forward traversal
    list<int>::iterator it = myList.begin();
    cout << "Forward traversal with modification: ";
    while (it != myList.end()) {
        // Write operation: increment each element by 2
        (*it) = (*it) + 2;
        // Read operation: print the modified value
        cout << (*it) << " ";
        // Move forward
        it++;
    }
    cout << endl;

    // Backward traversal
    list<int>::iterator itb = myList.end();
    cout << "Backward traversal with modification: ";
    while (itb != myList.begin()) {
        // Move backward
        itb--;
        // Write operation: increment each element by 5
        *itb = *itb + 5;
        // Read operation: print the modified value
        cout << (*itb) << " ";
    }
    cout << endl;

    return 0;
}