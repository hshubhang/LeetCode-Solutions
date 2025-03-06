from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Convert word list to a set for quick lookup
        if endWord not in wordSet:
            return 0  # If endWord is not in the list, no transformation is possible

        queue = deque([(beginWord, 1)])  # BFS queue with (word, transformation count)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps  # Found the shortest transformation sequence

            # Generate all possible one-letter transformations
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]  # Change one letter

                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)  # Remove from set to prevent re-visiting

        return 0  # No transformation sequence found
        