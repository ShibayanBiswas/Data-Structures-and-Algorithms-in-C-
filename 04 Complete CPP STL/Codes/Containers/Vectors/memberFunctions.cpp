#include<iostream>
#include<vector>

using namespace std;

int main() {
    
    // Creation of vectors
    vector<int> marks;
    vector<int> miles(10);           // Size: 10
    vector<int> distances(15, 5);    // Size: 15, each element initialized to 5

    // Accessing the first element using begin()
    cout << *(miles.begin()) << endl;

    // push_back()
    marks.push_back(10);
    marks.push_back(20);
    marks.push_back(30);
    marks.push_back(40);
    marks.push_back(50);

    // clear() - Uncomment to clear the vector
    // marks.clear();

    // insert() - Insert 50 at the beginning
    marks.insert(marks.begin(), 50);
    cout << marks[0] << endl;

    // erase() - Erase the first element
    marks.erase(marks.begin());
    cout << marks[0] << endl;

    // reserve() - Reserve space for 10 elements
    marks.reserve(10);

    // size() - Get the number of elements in the vector
    cout << "Size: " << marks.size() << endl;

    // capacity() - Get the capacity of the vector
    cout << "Capacity: " << marks.capacity() << endl;

    // max_size() - Get the maximum possible number of elements the vector can hold
    cout << marks.max_size() << endl;

    // pop_back() - Remove the last element
    marks.pop_back();

    // front() - Access the first element
    cout << marks.front() << endl;

    // back() - Access the last element
    cout << marks.back() << endl;

    // empty() - Check if the vector is empty
    if (marks.empty()) {
        cout << "Vector is empty" << endl;
    } else {
        cout << "Vector is not empty" << endl;
    }

    // operator[] - Access and modify the first element
    marks[0] = 100;
    cout << marks[0] << endl;

    // at() - Access the first element using at()
    cout << marks.at(0) << endl;

    // swap() - Swap the contents of marks and distances
    marks.swap(distances);

    // for-each loop to print elements of distances
    for (int i : distances) {
        cout << i << " ";
    }
    cout << endl;

    // for-each loop to print elements of marks
    for (int i : marks) {
        cout << i << " ";
    }
    cout << endl;

    // Loop using iterator to print elements of distances
    vector<int>::iterator it = distances.begin();
    while (it != distances.end()) {
        cout << *it << " ";
        it++;
    }
    cout << endl;

    return 0;
}