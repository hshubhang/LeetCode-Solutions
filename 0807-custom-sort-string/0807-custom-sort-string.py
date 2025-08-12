class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}

        order_list = list(order)
        input_string = list(s)

        for i in range(len(order_list)):
            hashmap[order_list[i]] = i

        print(hashmap)

        input_string.sort(key=lambda ch: hashmap.get(ch, len(order_list)))

        return "".join(input_string)

        
    