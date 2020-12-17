class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		if not text2 or not text1:
			return 0
		cols = len(text1)
		rows = len(text2)

		dp = [[0]*(cols+1) for _ in range(rows+1)] #  多加1 方便计算

		for r in range(rows):
			for c in range(cols):
				if text1[c]==text2[r]:
					dp[r][c] = dp[r-1][c-1] +1
				else:
					max(dp[r-1][c],dp[r][c-1])
