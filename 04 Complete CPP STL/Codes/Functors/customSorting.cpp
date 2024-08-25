#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Custom Comparator class for sorting in descending order
class Comparator {
public:
    bool operator()(int a, int b) {
        
        // Return true if 'a' should come after 'b' (i.e., for descending order)
        return a > b;
    }
};

int main() {
    vector<int> arr;

    // Adding elements to the vector
    arr.push_back(20);
    arr.push_back(10);
    arr.push_back(15);

    // Sorting the vector in descending order using the custom comparator
    sort(arr.begin(), arr.end(), Comparator());

    // Printing the sorted vector
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;

    return 0;
}