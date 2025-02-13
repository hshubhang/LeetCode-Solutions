class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0;
        int ans = 0;
        int curr = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 0){
                curr++;
                while (curr > k){
                    if (nums[left] == 0){
                        curr--;
                    }
                left++;
                }
            }
        ans = max(ans, i - left + 1);
        }
    return ans;
    }
};