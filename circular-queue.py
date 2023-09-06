class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.data = []
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if(self.isFull()):
            return False
        if(self.isEmpty()):
            self.head = 0
         
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = value
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if(self.isEmpty()):
            return False
        if(self.head == self.tail):
            self.head = -1
            self.tail = -1
            return True
        
        self.head = (self.head + 1) % self.size
        return True


    def Front(self):
        """
        :rtype: int
        """
        if(self.isEmpty()):
            return -1
        return self.data[self.head]

        

    def Rear(self):
        """
        :rtype: int
        """
        if(self.isEmpty()):
            return -1
        return self.data[self.tail]

        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.data) == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.tail +1) % self.size == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()