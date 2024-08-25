// Add two numbers represented by an array

class Solution {
public:
    string calc_Sum(int* a, int n, int* b, int m) {

        int carry = 0;
        string ans;
        int i = n - 1;
        int j = m - 1;

        // Add digits from both arrays
        while (i >= 0 && j >= 0) {
            int x = a[i] + b[j] + carry;
            int digit = x % 10;
            ans.push_back(digit + '0');
            carry = x / 10;
            i--, j--;
        }

        // Add remaining digits from array `a`
        while (i >= 0) {
            int x = a[i] + carry;
            int digit = x % 10;
            ans.push_back(digit + '0');
            carry = x / 10;
            i--;
        }

        // Add remaining digits from array `b`
        while (j >= 0) {
            int x = b[j] + carry;
            int digit = x % 10;
            ans.push_back(digit + '0');
            carry = x / 10;
            j--;
        }

        // If carry remains, add it as the most significant digit
        if (carry) {
            ans.push_back(carry + '0');
        }

        // Remove leading zeros (if any)
        while (ans.size() > 1 && ans.back() == '0') {
            ans.pop_back();
        }

        // Reverse the string to get the correct sum order
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

// Factorial of a large number

class Solution {
public:
    vector<int> factorial(int N) {
        
        vector<int> ans;
        ans.push_back(1);
        int carry = 0;

        // Multiply numbers from 2 to N
        for (int i = 2; i <= N; i++) {
            for (int j = 0; j < ans.size(); j++) {
                int x = ans[j] * i + carry;
                ans[j] = x % 10;
                carry = x / 10;
            }
            // Add carry digits to the vector
            while (carry) {
                ans.push_back(carry % 10);
                carry /= 10;
            }
        }

        // Reverse to get the correct order of the factorial
        reverse(ans.begin(), ans.end());
        return ans;
    }
};