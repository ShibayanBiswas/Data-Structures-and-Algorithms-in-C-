#include <iostream>
#include <list>
using namespace std;

int main() {
    
    // Creation of list
    list<int> myList;
    list<int> myList2(6, 5); // Creates a list of 6 elements, all initialized to 5

    // Insertion at the back
    myList.push_back(10);
    myList.push_back(20);
    myList.push_back(30);
    myList.push_back(10);
    myList.push_back(40);

    // Insertion at the front
    myList.push_front(100);

    // Insert an element at the beginning
    myList.insert(myList.begin(), 500);

    // Erase the first element
    myList.erase(myList.begin());

    // Pop from the back and front
    myList.pop_back();
    myList.pop_front();

    // Print the size of the list
    cout << "Size: " << myList.size() << endl;

    // Clear the list (optional, currently commented out)
    // myList.clear();

    // Check if the list is empty
    if (myList.empty()) {
        cout << "List is empty" << endl;
    } else {
        cout << "List is not empty" << endl;
    }

    // Access front and back elements
    cout << "Front: " << myList.front() << endl;
    cout << "Back: " << myList.back() << endl;

    // Iterate and print elements before removing
    cout << "Before removing: ";
    list<int>::iterator it = myList.begin();
    while (it != myList.end()) {
        cout << *it << " ";
        it++;
    }
    cout << endl;

    // Remove all occurrences of 10 from the list
    myList.remove(10);
    
    // Iterate and print elements after removing
    cout << "After removing: ";
    list<int>::iterator it2 = myList.begin();
    while (it2 != myList.end()) {
        cout << *it2 << " ";
        it2++;
    }
    cout << endl;

    // Swap contents of myList and myList2
    cout << "After swapping: ";
    myList2.swap(myList);
    
    // Iterate and print elements of myList after swapping
    list<int>::iterator it3 = myList.begin();
    while (it3 != myList.end()) {
        cout << *it3 << " ";
        it3++;
    }
    cout << endl;

    return 0;
}