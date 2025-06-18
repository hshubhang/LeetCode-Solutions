class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        main = x
        while x > 0:

            lastDigit = x % 10
            reverse = (reverse * 10) + lastDigit
            x = x // 10
            
        if reverse == main:
            return True
        else:
            return False
