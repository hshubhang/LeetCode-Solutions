class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        print(ransomNote_count)
        print(magazine_count)

        for i in ransomNote_count:
            if i not in magazine_count:
                return False
            elif i in magazine_count and ransomNote_count[i] > magazine_count[i]:
                return False


        return True