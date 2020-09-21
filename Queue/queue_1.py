'''
普通队列实现

先进先出  一个索引 一个列表构成


'''

class MyQueue:
    def __init__(self):
        self.data = []  #  队列
        self.p_start = 0 # 索引
    def enQueue(self,x):
        # Insert an element into the queue. Return true if the operation is successful
        self.data.append(x) #
        return True

    def deQueue(self):
        #   Delete an element from the queue. Return true if the operation is successful
        if self.isEmpty():
            return False
        self.p_start+=1
        return True


    def isEmpty(self):
        # Checks whether the queue is empty or not.
        return self.p_start > len(self.data)

    def Front(self):
        # Get the front item from the queue
        return self.data[self.p_start]   #  获取不到就报错了
