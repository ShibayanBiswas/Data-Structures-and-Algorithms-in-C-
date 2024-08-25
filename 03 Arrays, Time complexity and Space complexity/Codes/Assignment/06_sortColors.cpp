//leetcode 75: Sort Colors

class Solution {
public:
    //Counting Method
    void countingMethod(vector<int>& nums) {
        int zeros = 0, ones = 0, twos = 0;
        
        //count the occurrences of 0s, 1s, and 2s
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                zeros++;
            } else if (nums[i] == 1) {
                ones++;
            } else {
                twos++;
            }
        }
        
        //overwrite the array with the sorted values
        int i = 0;
        while (zeros--) {
            nums[i] = 0;
            i++;
        }
        while (ones--) {
            nums[i] = 1;
            i++;
        }
        while (twos--) {
            nums[i] = 2;
            i++;
        }
    }

    //Dutch National Flag Algorithm (Optimal Method)
    void sortColors(vector<int>& nums) {
        int l = 0, m = 0, h = nums.size() - 1;
        
        //iterate through the array and sort the colors
        while (m <= h) {
            if (nums[m] == 0) {
                swap(nums[l], nums[m]);
                l++, m++;
            } else if (nums[m] == 1) {
                m++;
            } else {
                swap(nums[m], nums[h]);
                h--;
            }
        }
    }
};