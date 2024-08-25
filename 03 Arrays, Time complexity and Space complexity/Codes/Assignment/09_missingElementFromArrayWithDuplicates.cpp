#include <iostream>
using namespace std;

//Visited method to find missing numbers
void findMissing(int *a, int n) {
    
    //Mark the visited elements by negating the corresponding index
    for (int i = 0; i < n; i++) {
        int index = abs(a[i]);
        if (a[index - 1] > 0) {
            a[index - 1] *= -1;
        }
    }
    //All positive indexes are missing numbers
    for (int i = 0; i < n; i++) {
        if (a[i] > 0)
            cout << i + 1 << " ";
    }
}

//Sort and swap method to find missing numbers
void sortAndSwapMethod(int *a, int n) {
    
    int i = 0;
    while (i < n) {
        int index = a[i] - 1;
        if (a[i] != a[index]) {
            swap(a[i], a[index]);
        } else {
            i++;
        }
    }
    //Find missing numbers after sorting
    for (int i = 0; i < n; i++) {
        if (a[i] != i + 1) {
            cout << i + 1 << " ";
        }
    }
}

int main() {
    int n;
    int a[] = {1, 3, 3, 3, 4};
    n = sizeof(a) / sizeof(int);

    //findMissing(a, n);  // Uncomment to use visited method
    sortAndSwapMethod(a, n);  // Default to sort and swap method

    return 0;
}