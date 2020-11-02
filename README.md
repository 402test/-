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

代码