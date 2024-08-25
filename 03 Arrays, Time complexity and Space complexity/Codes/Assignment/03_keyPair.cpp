//METHOD WITH TIME COMPLEXITY O(N^2) and SPACE COMPLEXITY O(1)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        int n = nums.size();
        
        // Brute-force approach
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    ans.push_back(i);
                    ans.push_back(j);
                    return ans;
                }
            }
        }
        return ans;
    }
};

// ANOTHER METHOD: TWO POINTER APPROACH
// Sorting is not helpful in this case, as you need to return the original indices
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        int n = nums.size();
        
        // Sort the array (not helpful for returning original indices)
        sort(nums.begin(), nums.end());
        int l = 0;
        int h = n - 1;
        
        while (l < h) {
            int csum = nums[l] + nums[h];
            if (csum == target) {
                ans.push_back(l);
                ans.push_back(h);
                return ans;
            } else if (csum > target) {
                h--;
            } else {
                l++;
            }
        }
        return ans;
    }
};