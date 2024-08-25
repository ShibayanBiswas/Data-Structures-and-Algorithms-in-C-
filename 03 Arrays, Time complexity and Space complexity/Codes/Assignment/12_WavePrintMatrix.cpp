#include <iostream>
#include <vector>
using namespace std;

// Function to print matrix in wave form

void wavePrintMatrix(vector<vector<int>> v) {
    
    int m = v.size();    // number of rows
    int n = v[0].size(); // number of columns

    for (int startCol = 0; startCol < n; startCol++) {
        // even column: Top to Bottom
        if ((startCol & 1) == 0) {
            for (int i = 0; i < m; i++) {
                cout << v[i][startCol] << " ";
            }
        } else {
            // odd column: Bottom to Top
            for (int i = m - 1; i >= 0; i--) {
                cout << v[i][startCol] << " ";
            }
        }
    }
}

int main() {
    vector<vector<int>> v{
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    wavePrintMatrix(v);

    return 0;
}