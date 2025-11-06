class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        max_active_seen = 0
        count_of_chars = Counter(croakOfFrogs)
        active = 0
        if len(set(count_of_chars.values())) != 1:
            return -1
        
        c_count = 0
        r_count = 0
        o_count = 0
        a_count = 0

        for i in croakOfFrogs:
            if i == "c":
                c_count += 1
                active += 1
                max_active_seen = max(max_active_seen, active)
                continue
            elif i == "r" and c_count:
                r_count += 1
                c_count -= 1
                continue
            elif i == "o" and r_count:
                o_count += 1
                r_count -= 1
            elif i == "a" and o_count:
                a_count += 1
                o_count -= 1
            elif i == "k" and a_count:
                a_count -= 1
                active -= 1
            else:
                return -1
            
        if c_count or r_count or o_count or a_count:
            return -1
        else:
            return max_active_seen





            
