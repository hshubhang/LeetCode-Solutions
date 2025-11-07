class Solution:
    def maximum69Number (self, num: int) -> int:
        ans_list = []


        ans_list = list(str(num))


        for i, char in enumerate(ans_list):

            if char == "6":
                ans_list[i] = "9"
                break

            
        return int("".join(ans_list))

            
        


        