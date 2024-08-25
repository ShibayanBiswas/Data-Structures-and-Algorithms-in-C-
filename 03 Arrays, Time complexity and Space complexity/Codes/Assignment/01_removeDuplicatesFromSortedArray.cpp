//leetcode 26: Remove Duplicates from Sorted Array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 1, j = 0;
        while (i < nums.size()) {
            if (nums[i] == nums[j]) {
                i++;
            } else {
                nums[++j] = nums[i++];
            }
        }
        return j + 1;
    }
};