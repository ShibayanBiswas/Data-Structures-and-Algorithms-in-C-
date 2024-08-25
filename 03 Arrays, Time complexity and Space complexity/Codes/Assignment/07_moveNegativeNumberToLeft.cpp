#include <iostream>
using namespace std;

//Move all negative numbers to the left using the Dutch National Flag Algorithm

void moveAllNegativeToLeft(int *a, int n) {
    int l = 0, h = n - 1;
    
    while (l < h) {
        if (a[l] < 0) {
            l++;  //move the left pointer if the element is negative
        } else if (a[h] > 0) {
            h--;  //move the right pointer if the element is positive
        } else {
            swap(a[l], a[h]);  //swap elements when a positive element is found on the left and a negative element is found on the right
        }
    }
}

int main() {
    int a[] = {1, 2, -3, 4, -5, 6};
    int n = sizeof(a) / sizeof(int);

    moveAllNegativeToLeft(a, n);

    //print the modified array
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    
    return 0;
}