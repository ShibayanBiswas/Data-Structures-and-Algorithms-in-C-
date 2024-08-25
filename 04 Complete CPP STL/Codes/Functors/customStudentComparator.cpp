#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Student class to hold marks and name
class Student {
public:
    int marks;
    string name;

    // Default constructor
    Student() {}

    // Parameterized constructor
    Student(int m, string n) {
        this->marks = m;
        this->name = n;
    }
};

// Comparator class for sorting students
class Comparator {
public:
    bool operator()(Student a, Student b) {
        // If marks are equal, sort by name in lexicographical order
        if (a.marks == b.marks) {
            return a.name < b.name;
        }
        // Otherwise, sort by marks in ascending order
        return a.marks < b.marks;
    }
};

int main() {
    vector<Student> arr;

    // Adding students to the vector
    arr.push_back(Student(90, "Shibayan"));
    arr.push_back(Student(90, "Lakshay"));
    arr.push_back(Student(95, "Sahil"));

    // Sorting students using the custom comparator
    sort(arr.begin(), arr.end(), Comparator());

    // Printing the sorted students
    for (Student a : arr) {
        cout << a.marks << " " << a.name << endl;
    }

    return 0;
}