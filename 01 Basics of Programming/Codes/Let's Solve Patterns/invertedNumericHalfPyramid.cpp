#include <iostream>
using namespace std;

int main(){

    //inverted numeric half pyramid
    int n;

    cout << "enter the value of n:";
    cin >> n;

    //outer loop
    for(int row = 0; row < n; row++){
        //inner loop
        for(int col = 0; col < n - row; col++){
            cout << (col + 1) << " ";
        }
        cout << endl;
    }

    return 0;
}