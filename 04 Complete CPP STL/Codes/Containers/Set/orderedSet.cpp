#include <iostream>
#include <set>
using namespace std;

int main(){
    
    // Creation of a set
    set<int> st;

    // Insertion of elements into the set
    st.insert(10);
    st.insert(15);
    st.insert(8);
    st.insert(4);

    // Traversing the set using an iterator
    set<int>:: iterator it = st.begin();
    while(it != st.end()){
        cout << *it << endl;
        it++;
    }

    // Displaying the size of the set
    cout << "size: " << st.size() << endl;

    // Finding an element in the set
    if(st.find(15) != st.end()){
        cout << "found" << endl;
    }
    else{
        cout << "not found" << endl;    
    }

    // Counting occurrences of an element in the set
    if(st.count(105) == 1){
        cout << "found";
    }
    else{
        cout << "not found" << endl;
    }

    // Clearing the set (removes all elements)
    st.clear();

    // Erasing elements (in this case, all elements from begin to end)
    st.erase(st.begin(), st.end());

    // Checking if the set is empty
    if(st.empty()==true){
        cout << "set is empty" << endl;
    }
    else{
        cout << "set is not empty" << endl;
    }

    return 0;
}