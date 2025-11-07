class Solution:
    def maximum69Number (self, num: int) -> int:
        ans_list = []

        
        heapq.heapify(ans_list)
        heapq.heappush(ans_list, -num)
        num_list = list(str(num))

        for i in range(len(num_list)):
            if num_list[i] == "9":
                num_list[i] = "6"
            elif num_list[i] == "6":
                num_list[i] = "9"

            heapq.heappush(ans_list, -(int("".join(num_list))))

            num_list = list(str(num))

        max_num = -heapq.heappop(ans_list)

        return max_num
            


        