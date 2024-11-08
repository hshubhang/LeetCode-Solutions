class Solution {
public:
    string removeDuplicates(string s) {
        std::stack<char>stack;
        int N = s.length();
        for(char ch: s){
            if (!stack.empty() && stack.top() == ch){
                stack.pop();
            }
            else
            {
                stack.push(ch);
            }
        }
        
        std::string result;
        while(!stack.empty()){
            result += stack.top();
            stack.pop();
        }
        std::reverse(result.begin(), result.end());
        return result;
    }
};