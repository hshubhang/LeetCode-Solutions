class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if not t or not s:
            return ""

        t_dict = Counter(t)
        required = len(t_dict)
        left, right = 0,0
        have_count = 0
        have_dict = defaultdict(int)
        res_left, res_right = 0, float('inf')

        while right < len(s):
            if s[right] in t_dict:
                have_dict[s[right]] += 1
            
                if have_dict[s[right]] == t_dict[s[right]]:
                    have_count += 1

            while left <= right and have_count == required:
                if right - left < res_right - res_left:
                    res_left, res_right = left, right

                if s[left] in t_dict:
                    have_dict[s[left]] -= 1
                    if have_dict[s[left]] < t_dict[s[left]]:
                        have_count -= 1
                left += 1
            right += 1
        return "" if res_right == float('inf') else s[res_left:res_right + 1]

            

            



            


            