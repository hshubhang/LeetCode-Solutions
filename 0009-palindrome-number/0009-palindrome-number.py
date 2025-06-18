class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_list = list(str(x))
        
        left, right = 0, len(x_list) - 1
        while left <= right:
            if x_list[left] == x_list[right]:
                left += 1
                right -=1
            else:
                return False

        return True
