#include<iostream>
#include<queue>
using namespace std;

int main(){
    
    // Creation of two queues
    queue<int> q;
    queue<int> r;

    // Insertion using push()
    q.push(10);
    q.push(20);
    q.push(30);
    q.push(40);
    r.push(100);
    r.push(200);

    // Displaying the size of queue q
    cout << "Size of q: " << q.size() << endl;

    // Removing the front element using pop()
    q.pop();

    // Checking if the queue q is empty
    if(q.empty()){
        cout << "Queue q is empty" << endl;
    }
    else{
        cout << "Queue q is not empty" << endl;
    }

    // Accessing the front element
    cout << "Front of q: " << q.front() << endl;

    // Accessing the back element
    cout << "Back of q: " << q.back() << endl;

    // Swapping contents of q and r
    q.swap(r);

    // After swapping, display the front elements of both queues
    cout << "After swap, front of q: " << q.front() << ", front of r: " << r.front() << endl;

    return 0;
}