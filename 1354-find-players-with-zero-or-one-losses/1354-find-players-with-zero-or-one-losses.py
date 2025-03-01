from collections import defaultdict
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_hashmap = defaultdict(int)
        winner_hashmap = set()

        for winner, loser in matches:
            winner_hashmap.add(winner)
            loser_hashmap[loser] += 1

        arr1 = sorted([player for player in winner_hashmap if player not in loser_hashmap])

        arr2 = sorted([player for player, losses in loser_hashmap.items() if losses == 1])

        return [arr1, arr2]
        