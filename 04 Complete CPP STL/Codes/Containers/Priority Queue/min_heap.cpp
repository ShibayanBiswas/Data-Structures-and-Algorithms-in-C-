#include<iostream>
#include<queue>
using namespace std;

int main(){
    
    // Min-heap: smallest value has the highest priority
    priority_queue<int, vector<int>, greater<int>> pq;

    // Insertion of elements
    pq.push(100);
    pq.push(50);
    pq.push(75);
    pq.push(200);

    // Access the top element (the highest priority element, which is the minimum value in a min-heap)
    cout << "Top element: " << pq.top() << endl;

    // Remove the top element (highest priority element)
    pq.pop();

    // After popping, the next top element (smallest value) will be the new minimum
    cout << "New top element after pop: " << pq.top() << endl;

    return 0;
}