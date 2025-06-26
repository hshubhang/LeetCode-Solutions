import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowercase = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]+', '', lowercase)
        print(cleaned)
        sList = list(cleaned)
       
        left = 0
        right = len(sList) - 1

        while left < right:

            if sList[left] == sList[right]:
                left+= 1
                right -= 1
            else:
                return False

        return True