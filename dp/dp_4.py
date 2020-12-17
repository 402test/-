from typing import List

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         if not s or not wordDict:
#             return False
#         slen = len(s)
#         dp = [False for _ in range(slen+1)]
#         dp[0] = True
#         for i in range(0,slen):
#             for j in range(0,slen):
#                 print(s[i:slen-j])
#                 if dp[i] and s[i:slen-j] in wordDict:
#                     print(slen-j)
#                     dp[slen-j] = True
#         return dp[-1]
               
       


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def helper(index):
#             if s[index:] in List:
#                 return True
#             for w in wordDict:
#                 if s[index:index+len(w)] == w and helper(index+len(w))
#         return helper(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        lens = len(s)

        for i in range(lens):
            for w in wordDict:
                lenw = len(w)
                if s[i:i+lenw] == w and dp[i] and len(w)+i <lens+1:
                    dp[lenw+i] = True
        return dp[-1]

s = Solution()

print(s.wordBreak('leetcode',['leet','code']))



# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         import functools
#         #@functools.lru_cache(None)
#         def solution(index):
#             if s[index:] in wordDict:
#                 return True
#             for w in wordDict:
#                 if s[index:index + len(w)] == w and solution(index + len(w)):
#                     return True
#             return False

#         return solution(0)
# s = Solution()

# print(s.wordBreak('leetcode',['leet','code']))