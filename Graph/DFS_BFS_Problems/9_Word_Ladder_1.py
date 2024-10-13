"""
https://leetcode.com/problems/word-ladder/description/


"""

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        n=len(beginWord)
        q=deque()

        q.append((beginWord, 1))
        alphabet = ["a","b","c","d","e","f",
                    "g","h","i","j","k","l",
                    "m","n","o","p","q","r",
                    "s","t","u","v","w","x",
                    "y","z"]
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            # w = word.copy()

            for i in range(n):
                for alpha in alphabet:
                    w = word[: i] + alpha + word[i + 1:]
                    if w in wordList:
                        wordList.remove(w)
                        q.append((w, level+1))
        return 0

