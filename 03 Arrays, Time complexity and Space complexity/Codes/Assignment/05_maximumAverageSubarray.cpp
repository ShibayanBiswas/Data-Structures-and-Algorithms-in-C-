//leetcode 643: Maximum Average Subarray I

class Solution {
public:
    //Brute Force Method: O(N^2)
    double bruteForce(vector<int>& nums, int& k) {
        int maxSum = INT_MIN;
        int i = 0, j = k - 1;
        
        while (j < nums.size()) {
            int sum = 0;
            for (int y = i; y <= j; y++)
                sum += nums[y];
            maxSum = max(maxSum, sum);
            i++, j++;
        }
        
        double maxAvg = maxSum / (double)k;
        return maxAvg;
    }
    
    //Sliding Window Method: O(N)
    double slidingWindow(vector<int>& nums, int& k) {
        int i = 0, j = k - 1;
        int sum = 0;
        
        //initialize sum of the first k elements
        for (int y = i; y <= j; y++)
            sum += nums[y];
        
        int maxSum = sum;
        j++;
        
        //slide the window across the array
        while (j < nums.size()) {
            sum -= nums[i++];  //remove the first element of the previous window
            sum += nums[j++];  //add the new element to the current window
            maxSum = max(maxSum, sum);
        }
        
        double maxAvg = maxSum / (double)k;
        return maxAvg;
    }

    double findMaxAverage(vector<int>& nums, int k) {
        //return bruteForce(nums, k);  //O(N^2) approach
        return slidingWindow(nums, k);  //O(N) approach
    }
};