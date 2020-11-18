# 数据结构

队列，栈 ，二叉树，链表，桶。





## 队列 & 栈

*2020-9-18打卡*

队列和栈是两种不同的线性数据结构：前者先入先出，后者后入先出

![img](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/14/screen-shot-2018-05-03-at-151021.png)

在 FIFO 数据结构中，将首先处理添加到队列中的第一个元素。

如上图所示，队列是典型的 FIFO 数据结构。插入（insert）操作也称作入队（enqueue），新元素始终被添加在队列的末尾。 删除（delete）操作也被称为出队（dequeue)。 你只能移除第一个元素



### 设计普通队列
[代码](https://github.com/402test/data-structure/blob/master/Queue/queue_1.py)


普通队列无法做到循环使用，随着起始指针的移动，浪费了越来越多的空间。

### 设计循环队列
[代码](https://github.com/402test/data-structure/blob/master/Queue/queue_2.py)
- 时间复杂度：O(1)。该数据结构中，所有方法都具有恒定的时间复杂度。
- 空间复杂度：O(N)，其中 N 是队列的预分配容量。*循环队列的整个生命周期中，都持有该预分配的空间。*



从并发性来看，该循环队列是线程不安全的。

![img](https://pic.leetcode-cn.com/Figures/622/622_concurrency.png)

这种情况称为竞态条件。加线程锁就可以了



```python
from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        # the additional attribute to protect the access of our queue
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # automatically acquire the lock when entering the block
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
        # automatically release the lock when leaving the block
        return True

```
### 队列练习

#### 岛屿数量

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

```
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1

```

```
输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

```



[代码](https://github.com/402test/data-structure/blob/master/Queue/queue_3.py)

[力扣解答](https://github.com/402test/data-structure/blob/master/Queue/leetcode-queue-1.py)

[力扣解答](https://github.com/402test/data-structure/blob/master/Queue/leetcode-queue-2.py)

#### 打开转盘锁



你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

 

示例 1:

```
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定
```

。
示例 2:

```
输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
```


示例 3:

```
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
```


示例 4:

```
输入: deadends = ["0000"], target = "8888"
输出：-1
```


提示：

死亡列表 deadends 的长度范围为 [1, 500]。
目标数字 target 不会在 deadends 之中。
每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。

[代码](https://github.com/402test/data-structure/blob/master/Queue/queue_4.py)

2020-10-15






#### 完全平方数

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

```
输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
```


示例 2:

```
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
```

学习了动态规划在做

#### 动态规划

动态规划问题1

```
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
```

[代码](https://github.com/402test/data-structure/blob/master/Queue/queue_5.py)

动态规划问题1

打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

```
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

```



解析

1. 偷窃第K间房屋，那么就不能偷窃K-1间房屋，偷窃总金额为前 k*−2 间房屋的最高总金额与第 k* 间房屋的金额之和。
2. 不偷窃第 k间房屋，偷窃总金额为前k−1 间房屋的最高总金额。

用 dp[i]表示前 i 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：

*dp*[*i*]=max(*dp*[*i*−2]+*nums*[*i*],*dp*[*i*−1])

边界条件为：
$$
\left\{
\begin{aligned}
&dp[0] = nums[0] 只有一间房屋，则偷窃该房屋 \\
&dp[1]=max(nums[0],nums[1]) 只有两间房屋，选择较高的
\end{aligned}
\right.
$$


最终dp[n-1] 是答案，n是数组长度

[代码](https://github.com/402test/data-structure/blob/master/dp/dp_1.py)



打家劫舍2

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

```
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

```
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```



思路和之前一样，不过在存在第一个和最后一个偷不偷。

1. 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1 ；
2. 在不偷窃最后一个房子的情况下（即 nums[:n-1]），最大金额是 p2 。
3. **综合偷窃最大金额：** 为以上两种情况的较大值，即 max(p1,p2) 。

[代码](https://github.com/402test/data-structure/blob/master/dp/dp_2.py)

最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。



```
示例 1:
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
```

