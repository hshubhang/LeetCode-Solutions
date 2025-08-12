class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = defaultdict(int)

        parsed_string1 = s1.split(" ")
        parsed_string2 = s2.split(" ")

        for i in range(len(parsed_string1)):
            hashmap[parsed_string1[i]] += 1
        for j in range(len(parsed_string2)):
            hashmap[parsed_string2[j]] += 1

        return [word for word in hashmap if hashmap[word] == 1]