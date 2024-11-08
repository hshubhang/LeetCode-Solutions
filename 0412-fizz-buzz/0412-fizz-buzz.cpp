class Solution {
public:
    vector<string> fizzBuzz(int n) {

        std::vector<std::string> ans;
        for(int i = 1; i < n + 1; i++){
            if (i % 3 == 0 && i % 5 == 0){

                ans.push_back("FizzBuzz");
            }
            else if(i % 3 == 0){

                ans.push_back("Fizz");
            }
            else if(i % 5 == 0){
                
                ans.push_back("Buzz");
            }
            else {
                std::string strNum = std::to_string(i);
                ans.push_back(strNum);

            }

            }
        return ans;
        }
};