#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
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

// Comparator class to define the priority in the priority queue
class Comparator {
public:
    bool operator()(Student a, Student b) {
        // Criteria: Student with max marks has high priority (max-heap)
        return a.marks < b.marks;
    }
};

int main() {
    // Priority queue with custom comparator to create a max-heap
    priority_queue<Student, vector<Student>, Comparator> pq;
    
    // Adding students to the priority queue
    pq.push(Student(90, "Shibayan"));
    pq.push(Student(67, "Tony"));
    pq.push(Student(89, "Lakshay"));
    pq.push(Student(72, "Love"));

    // Display the top student (highest marks)
    cout << "Top student: " << pq.top().marks << " " << pq.top().name << endl;

    return 0;
}