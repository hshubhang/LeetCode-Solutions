class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left, best, curr;
        left = best = curr = 0;
        for (int right = 0; right < prices.size(); right++){
            while (prices[left] > prices[right]){
                left++;
            }
        curr = prices[right] - prices[left];
        best = max(best, curr);
        }
    return best;
    }
};