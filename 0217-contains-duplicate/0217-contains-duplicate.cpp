class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::set<int> s = set(begin(nums), end(nums));
        return s.size() != nums.size();
    }
};