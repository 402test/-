'''
岛屿数量计算

思路
两层循环迭代所有的  节点 。 当数字为 1 的时候 。 加入一个维护的队列 。  然后 while 次队列。  在循环里面  出队。 然后 查询 该出队的节点的 上写左右 有没有等于1 的节点
如果有 就添加进队列 并置为0 .  while 循环退出  代码 这一个岛屿都找完了。 然后找下一个岛屿


'''
class Solution:
    def numIslands(self, grid):



        self.grid = grid
        nums = 0

        for row in range(len( self.grid)):
            for d in range(0,len(self.grid[row])):
                if  self.grid[row][d]=='1':
                    self.find_k(row,d)
                    nums+=1
        return nums

    def find_k(self,r,d):
        L_one = [[r,d]]
        while L_one:
            print(L_one)
            k = L_one.pop(0)
            top = k[0]-1
            down = k[0]+1
            left = k[1]-1
            right = k[1]+1

            if top>=0 and self.grid[top][k[1]] =='1':
                L_one.append([top,k[1]])
                self.grid[top][k[1]] = 0

            if down < len(self.grid) and self.grid[down][k[1]] =='1':
               L_one.append([down,k[1]])
               self.grid[down][k[1]] =0

            if left>=0 and self.grid[k[0]][left] =='1':
                L_one.append([k[0],left])
                self.grid[k[0]][left] = '0'

            if right<len(self.grid[k[0]]) and self.grid[k[0]][right] =='1':
                L_one.append([k[0],right])
                self.grid[k[0]][right] =0


#
# s = Solution()
# print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))