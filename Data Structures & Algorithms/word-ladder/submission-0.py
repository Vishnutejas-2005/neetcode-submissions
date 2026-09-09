class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque

        if endWord not in wordList:
            return 0
        n = len(beginWord)
        que = deque()
        visited = set()

        visited.add(beginWord)
        que.append(beginWord)

        level = 0
        while que:
            level += 1
            k = len(que)
            for _ in range(k):
                curr = que.popleft()
                if curr == endWord:
                    return level
                for i in range(n):
                    for j in range(26):
                        new_word =  curr[:i] + chr(j+ord("a")) + curr[i+1:]
                        if new_word in wordList and new_word not in visited:
                            que.append(new_word)
                            visited.add(new_word)

        return 0
        