from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        n=len(beginWord)
        output = []

        q=deque()
        q.append([beginWord])
        alphabet = ["a","b","c","d","e","f",
                    "g","h","i","j","k","l",
                    "m","n","o","p","q","r",
                    "s","t","u","v","w","x",
                    "y","z"]
        level = 0
        while q:
            sequence = q.popleft()
            word = sequence[-1]

            if len(sequence) > level:
                level += 1
                for i in sequence:
                    if i in wordList:
                        wordList.remove(i)

            if word == endWord:
                if output==[]:
                    output.append(sequence)
                elif len(output[0]) == len(sequence):
                    output.append(sequence)

            for i in range(n):
                for alpha in alphabet:
                    w = word[: i] + alpha + word[i + 1:]
                    if w in wordList:
                        # wordList.remove(w)
                        q.append(sequence + [w])
        return output      


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol = Solution()
print(sol.findLadders(beginWord, endWord, wordList))
