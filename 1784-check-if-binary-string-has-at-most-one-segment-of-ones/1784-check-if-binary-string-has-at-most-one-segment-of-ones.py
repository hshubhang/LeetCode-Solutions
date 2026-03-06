class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segment_count = 0
        no_count = Counter(s)
        in_ones = True
        

        for i in range(len(s)):
            if s[i] == "1":
                in_ones = True
            else:
                if in_ones:
                    segment_count += 1
                    in_ones = False

            
        if in_ones:
            segment_count += 1

        return segment_count <= 1




        