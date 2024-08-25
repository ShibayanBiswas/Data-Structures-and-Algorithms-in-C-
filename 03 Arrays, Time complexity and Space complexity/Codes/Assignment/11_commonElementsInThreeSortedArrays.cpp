class Solution {
public:
    vector<int> commonElements(int A[], int B[], int C[], int n1, int n2, int n3) {
        
        vector<int> ans;
        set<int> st;  // to store unique common elements
        int i = 0, j = 0, k = 0;  // initializing indices for three arrays

        // Traverse all three arrays simultaneously
        while (i < n1 && j < n2 && k < n3) {
            // If the current elements in all three arrays are equal, it is a common element
            if (A[i] == B[j] && B[j] == C[k]) {
                st.insert(A[i]);  // insert into set to avoid duplicates
                i++, j++, k++;  // move to the next element in all arrays
            }
            // If A[i] is smaller, move to the next element in A
            else if (A[i] < B[j]) {
                i++;
            }
            // If B[j] is smaller, move to the next element in B
            else if (B[j] < C[k]) {
                j++;
            }
            // If C[k] is smaller, move to the next element in C
            else {
                k++;
            }
        }

        // Transfer elements from the set to the result vector
        for (auto it : st) {
            ans.push_back(it);
        }

        return ans;
    }
};