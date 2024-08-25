#include <iostream>
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

// Functor (function object) class for comparing students based on marks
class StudentComparator {
public:
    bool operator()(Student a, Student b) {
        // Compare students by marks in ascending order
        return a.marks < b.marks;
    }
};

int main() {
    // Creating two Student objects
    Student s1(95, "Shibayan");
    Student s2(93, "Lakshay");

    // Creating an instance of the StudentComparator functor
    StudentComparator cmp;

    // Using the functor to compare the two students
    if (cmp(s1, s2)) {
        cout << "Shibayan has lesser marks" << endl;
    } else {
        cout << "Shibayan has more marks" << endl;
    }

    return 0;
}