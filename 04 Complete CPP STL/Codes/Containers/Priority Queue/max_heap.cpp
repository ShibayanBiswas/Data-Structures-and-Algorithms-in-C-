#include<iostream>
#include<queue>
using namespace std;

int main(){
    // Creation of a priority_queue
    priority_queue<int> pq;  // Max-heap by default, meaning highest value has the highest priority

    // Insertion of elements
    pq.push(10);
    pq.push(25);
    pq.push(55);
    pq.push(21);

    // Access the top element (the highest priority element, which is the maximum value in a max-heap)
    cout << "Top element: " << pq.top() << endl;

    // Remove the top element (highest priority element)
    pq.pop();

    // Print the size of the priority_queue
    cout << "Size after pop: " << pq.size() << endl;

    // Check if the priority_queue is empty
    if(pq.empty()) {
        cout << "Priority queue is empty" << endl;
    } else {
        cout << "Priority queue is not empty" << endl;
    }
    
    return 0;
}