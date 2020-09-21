'''

循环队列
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。


'''


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k  #  一个固定大小的数组
        self.headIndex = 0 # 保存队首
        self.count = 0 # 当前队列的实际长度  也就是保存的元素数量
        self.capacity = k #  队列容量

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        添加元素  需要先判断队列是否满了  如果没有满  则将队尾的元素赋值   不能使用append  不然队列会超出最大长度

        """
        if self.isFull():
            return False
        # 覆盖  队尾部的下一个元素   获取 队尾在哪里 ---   队首 +  元素数量 -1    就等于 队尾 。   但是现在是循环的一圈 .  所以 （队首 +  元素数量 -1 ）mod capacity  。也就是取余 ，领悟一下
        self.queue[(self.headIndex+self.count)%self.capacity] = value  #  因为覆盖队尾下一个元素    所以不用  -1
        self.count+=1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.

        删除操作 就是队首向前移动一位
        """
        if self.isEmpty():
            return False

        #self.headIndex+=1   因为是循环的  所以不能直接加1
        self.headIndex = (self.headIndex+1) % self.capacity
        self.count-=1
        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        取队尾
        """
        if self.isEmpty():
            return self.queue[(self.headIndex+self.count - 1) % self.capacity]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# k = 10
# value = 4
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()