#include <iostream>
#include <stack>
using namespace std;

int main(){

    // Creation of the stack
    stack<int> st;
    
    // Inserting elements into the stack
    st.push(10);
    st.push(20);
    st.push(30);
    st.push(40);

    // Displaying the size of the stack
    cout << "size: " << st.size() << endl; // Output: 4

    // Removing the top element
    st.pop();

    // Displaying the top element after pop
    cout << st.top() << endl; // Output: 30
    
    // Checking if the stack is empty
    if(st.empty() == true){
        cout << "stack is empty" << endl;
    }
    else{
        cout << "stack is not empty" << endl; // Output: stack is not empty
    }
    
    return 0;
}