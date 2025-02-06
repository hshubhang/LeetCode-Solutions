class Solution {
public:
    void reverseString(vector<char>& s) {
        int first = 0;
        int last = s.size() - 1;
        while(first<last){
            char temp = s[last];
            s[last] = s[first];
            s[first]= temp;
            first++;
            last--;
        }

    }
};