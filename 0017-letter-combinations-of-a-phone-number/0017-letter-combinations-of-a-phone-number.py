class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(currchar, currstr):
            if len(currstr) == len(digits):
                res.append(currstr)
                return
            
            for ch in letters[digits[currchar]]:
                backtrack(currchar + 1, currstr + ch)

        if digits:    
            backtrack(0, "")

        return res


            