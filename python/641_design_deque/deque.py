class MyCircularDeque:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.data = [-1] * k
        self.capacity = k
        self.real_cap = 0
        self.__front, self.__rear = 0, 1

    def insertFront(self, value: 'int') -> 'bool':
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.real_cap == self.capacity:
            return False    # deque is full now
        else:
            self.real_cap += 1
            self.data[self.__front] = value
            self.__front = (self.__front - 1 + self.capacity) % self.capacity
            
        return True
        

    def insertLast(self, value: 'int') -> 'bool':
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.real_cap == self.capacity:
            return False
        else:
            self.real_cap += 1
            self.data[self.__rear] = value
            self.__rear = (self.__rear + 1 + self.capacity) % self.capacity
        
        return True
        

    def deleteFront(self) -> 'bool':
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.real_cap -= 1
            self.__front = (self.__front + 1 + self.capacity) % self.capacity
            self.data[self.__front] = -1
        
        return True
        

    def deleteLast(self) -> 'bool':
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.real_cap -= 1
            self.__rear = (self.__rear - 1 + self.capacity) % self.capacity
            self.data[self.__rear] = -1
        
        return True
        

    def getFront(self) -> 'int':
        """
        Get the front item from the deque.
        """
        return self.data[(self.__front + 1 + self.capacity) % self.capacity]
        

    def getRear(self) -> 'int':
        """
        Get the last item from the deque.
        """
        return self.data[(self.__rear - 1 + self.capacity) % self.capacity]
        

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular deque is empty or not.
        """
        return self.real_cap == 0
        

    def isFull(self) -> 'bool':
        """
        Checks whether the circular deque is full or not.
        """
        return self.real_cap == self.capacity