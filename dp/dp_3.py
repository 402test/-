class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		if not text2 or not text1:
			return 0

		cols = len(text1)
		rows = len(text2)
		dp = [[0]*(cols+1) for _ in range(0,rows+1)]# 二维表格  方便计算  多加了一圈 0
		for i in range(0,rows):
			for j in range(0,cols):
				if text2[i] == text1[j]:
					# 当相同的时候  则使用上一次dp 的值 +1
					dp[i][j] = dp[i-1][j-1]+1
				else:
					 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
		print(dp)
		return dp[-2][-2]