#include <iostream>
#include <deque>
using namespace std;

int main() {
    
    // Creation of deque
    deque<int> dq;

    // Insertion at the back
    dq.push_back(10);
    dq.push_back(20);
    dq.push_back(30);
    dq.push_back(40);

    // Insertion at the front
    dq.push_front(100);
    dq.push_front(200);

    // Clear the deque (optional, currently commented out)
    // dq.clear();

    // Insert an element at the beginning
    dq.insert(dq.begin(), 101);

    // Erase the first element
    dq.erase(dq.begin());

    // Pop from the front and back
    dq.pop_front();
    dq.pop_back();

    // Print size of the deque
    cout << "Size: " << dq.size() << endl;

    // Access front element
    cout << "Front: " << dq.front() << endl;

    // Access back element
    cout << "Back: " << dq.back() << endl;

    // Check if deque is empty
    if (dq.empty()) {
        cout << "Deque is empty" << endl;
    } else {
        cout << "Deque is not empty" << endl;
    }

    // Iterate over deque and print elements
    deque<int>::iterator it = dq.begin();
    while (it != dq.end()) {
        cout << *it << " ";
        it++;
    }
    cout << endl;

    // Access elements using operator[]
    cout << "Element at index 0: " << dq[0] << endl;

    // Access elements using at() method
    cout << "Element at index 3: " << dq.at(3) << endl;

    return 0;
}