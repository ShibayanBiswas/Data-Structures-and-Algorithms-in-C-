#include <iostream>
using namespace std;

//reverse an array

void reverseArray(int arr[], int n) {

    int l = 0, h = n - 1;
    while (l < h) {
        swap(arr[l++], arr[h--]);
    }
}

int main() {
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80};
    int n = 8;

    reverse(arr, arr + n);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}