#include<iostream>
#include<vector>

using namespace std;

// 2D array using vector

int main() {

    // Creation of a 2D vector with 5 rows and 4 columns initialized to 0
    vector<vector<int>> arr(5, vector<int>(4, 0));

    // Get total rows and columns
    int totalRows = arr.size();
    int totalColumns = arr[0].size();

    // Jagged array creation (rows with different column sizes)
    vector<vector<int>> brr(4);
    brr[0] = vector<int>(4);  // 1st row with 4 columns
    brr[1] = vector<int>(2);  // 2nd row with 2 columns
    brr[2] = vector<int>(5);  // 3rd row with 5 columns
    brr[3] = vector<int>(3);  // 4th row with 3 columns

    // Get the total number of rows in the jagged array
    int totalRowCount = brr.size();

    // To access the number of columns in a specific row:
    // int totalColumnCount = brr[i].size();  // Example usage: for row i

    return 0;
}