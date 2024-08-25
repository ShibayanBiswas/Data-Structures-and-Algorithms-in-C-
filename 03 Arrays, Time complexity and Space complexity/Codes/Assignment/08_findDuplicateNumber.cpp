// Leetcode 287: Find the Duplicate Number

class Solution {
public:
    //Negative marking method
    int findDuplicate(vector<int>& nums) {
        int ans = -1;
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]);
            if (nums[index] < 0) {
                ans = index;
                break;
            }
            nums[index] *= -1;
        }
        return ans;
    }

    //Positioning method
    int findDuplicatePositioning(vector<int>& nums) {
        while (nums[0] != nums[nums[0]]) {
            swap(nums[0], nums[nums[0]]);
        }
        return nums[0];
    }
};