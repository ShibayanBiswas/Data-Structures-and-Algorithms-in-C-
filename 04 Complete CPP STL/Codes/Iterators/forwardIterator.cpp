#include <iostream>
#include <vector>
#include <forward_list>
using namespace std;

// Forward Iterator
int main() {
    
    forward_list<int> list;
    list.push_front(10);
    list.push_front(20);
    list.push_front(30);

    // Traverse and modify the list
    forward_list<int>::iterator it = list.begin();
    while (it != list.end()) {
        // Read and print the value
        cout << *it << " ";
        // Modify the value by adding 5
        (*it) = (*it) + 5;
        // Move forward
        it++;
    }
    cout << endl;

    // Traverse again to print modified values
    it = list.begin();
    while (it != list.end()) {
        cout << *it << " ";
        it++;
    }
    cout << endl;

    return 0;
}