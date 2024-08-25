#include <iostream>
using namespace std;

// Functor (Function Object) class
class functorOne {
public:
    bool operator()(int a, int b) {
        // Compare in descending order
        // If a > b, return true (indicating a should be placed before b)
        return a > b;
    }
};

int main() {
    functorOne cmp; // Create an instance of the functor

    // Use the functor to compare two integers
    if (cmp(10, 5) == true) {
        cout << "10 is greater than 5" << endl;
    } else {
        cout << "10 is less than 5" << endl;
    }

    return 0;
}