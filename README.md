# 数据结构

队列，栈 ，二叉树，链表，桶。





## 队列 & 栈

*2020-9-18打卡*

队列和栈是两种不同的线性数据结构：前者先入先出，后者后入先出

![img](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/14/screen-shot-2018-05-03-at-151021.png)

在 FIFO 数据结构中，将首先处理添加到队列中的第一个元素。

如上图所示，队列是典型的 FIFO 数据结构。插入（insert）操作也称作入队（enqueue），新元素始终被添加在队列的末尾。 删除（delete）操作也被称为出队（dequeue)。 你只能移除第一个元素



### 设计普通队列



普通队列无法做到循环使用，随着起始指针的移动，浪费了越来越多的空间。

### 设计循环队列

- 时间复杂度：\mathcal{O}(1)O(1)。该数据结构中，所有方法都具有恒定的时间复杂度。
- 空间复杂度：\mathcal{O}(N)O(*N*)，其中 N*N* 是队列的预分配容量。*循环队列的整个生命周期中，都持有该预分配的空间。*



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

