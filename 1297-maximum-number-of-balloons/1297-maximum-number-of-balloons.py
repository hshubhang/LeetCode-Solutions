class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = defaultdict(int)
        balloon_dict["b"] = 0
        balloon_dict["a"] = 0
        balloon_dict["l"] = 0
        balloon_dict["l"] = 0
        balloon_dict["o"] = 0
        balloon_dict["n"] = 0

        for i in list(text):
            if i in balloon_dict:
                balloon_dict[i] += 1

        balloon_dict["l"] //= 2
        balloon_dict["o"] //= 2

        return min(balloon_dict["b"], balloon_dict["a"], balloon_dict["l"], balloon_dict["o"], balloon_dict["n"])


