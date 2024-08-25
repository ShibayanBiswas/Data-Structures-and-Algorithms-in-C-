class Solution {
public:
    int firstRepeated(int a[], int n) {

        /* Brute-force approach: O(N^2)

        for(int i = 0; i < n; i++) {
            bool isRepeated = false;
            for(int j = i + 1; j < n; j++) {
                if(a[i] == a[j]) {
                    isRepeated = true;
                    return i + 1;  // Return the 1-based index of the first repeated element
                }
            }
        }
        return -1;  // If no repeated element is found
        */

        // Optimized approach using Hashing: O(N)
        unordered_map<int, int> hash;

        // Store the frequency of each element in the array
        for (int i = 0; i < n; i++) {
            hash[a[i]]++;
        }

        // Traverse the array again to find the first element with frequency > 1
        for (int i = 0; i < n; i++) {
            if (hash[a[i]] > 1) {
                return i + 1;  // Return the 1-based index of the first repeated element
            }
        }

        return -1;  // If no repeated element is found
    }
};