# 打开转盘锁  解题思路就是  以 0000 为起点  计算出每走一步可能出现得节点 
#  例如   开局0000  走一步 可能是  1000 9000 0100 0900  .。。。。。  一共8个  

#   走两步可能是  1100  1900 9900 .。。。。。。。   一共 64 个     但是 要去重  维护一个set 去重 

# 然后使用到 collections  的 deque   实现了在两端快速添加(append)和弹出(pop)  |   不用这个也可以。
from typing import List
import collections
class Solution:
	def openLock(self, deadends: List[str], target: str) -> int:
		def helper(node):
			# 接受一个节点  返回 它相邻的 8个节点  
			# 以生成器的形式  返回节点
			for i in range(4):
				x = int(node[i])
				for d in (-1,1):
					y = (x+d)%10
					yield node[:i]+str(y)+node[i+1:]

		dead = set(deadends)
		queue = collections.deque([('0000',0)])
		seen = {'0000'} #  已经遍历到了的  避免重复

		while queue:
			node,path = queue.popleft()
			if node == target : return path
			if node in dead:  continue
			for nei in helper(node):
				if nei not in seen:
					seen.add(nei)
					queue.append([nei,path+1])
		return -1




