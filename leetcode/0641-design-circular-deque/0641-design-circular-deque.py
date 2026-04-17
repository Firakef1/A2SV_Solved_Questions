class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:


    def __init__(self, k: int):
        # Use self so these belong to the INSTANCE, not the CLASS
        self.MAX_SIZE = k
        self.CUR_SIZE = 0
        self.front = None
        self.end = None


    def insertFront(self, value: int) -> bool:
        # print(self.MAX_SIZE, self.CUR_SIZE)

        if self.CUR_SIZE == self.MAX_SIZE:
            return False
        
        node = Node(value)

        if not self.end:
            self.end = node
            self.front = node
        else:

            node.next = self.front
            self.front.prev = node

            self.front = node

        self.CUR_SIZE += 1
        
        return True

    def insertLast(self, value: int) -> bool:
        # print(self.MAX_SIZE, self.CUR_SIZE)

        if self.CUR_SIZE == self.MAX_SIZE:
            return False
        
        node = Node(value)

        if not self.front:
            self.front = node
            self.end = node
        else:
            node.prev = self.end
            self.end.next = node
            
            self.end = node

        self.CUR_SIZE+= 1
        
        return True

        
    def deleteFront(self) -> bool:
        if self.CUR_SIZE == 0:
            return False
        
        if self.CUR_SIZE == 1:
            self.front = None
            self.end = None
            self.CUR_SIZE -= 1
            return True

        self.front = self.front.next
        self.front.prev = None
        self.CUR_SIZE -= 1
        return True

    def deleteLast(self) -> bool:
        if self.CUR_SIZE == 0:
            return False
        
        if self.CUR_SIZE == 1:
            self.front = None
            self.end = None
            self.CUR_SIZE -= 1
            return True
        
        self.end = self.end.prev
        self.end.next = None
        self.CUR_SIZE -= 1
        return True

    def getFront(self) -> int:
        if not self.CUR_SIZE:
            return -1
        
        return self.front.val

    def getRear(self) -> int:
        if not self.CUR_SIZE:
            return -1
        
        return self.end.val

    def isEmpty(self) -> bool:
        if self.CUR_SIZE == 0:
            return True
        
        return False

    def isFull(self) -> bool:
        if self.CUR_SIZE == self.MAX_SIZE:
            return True
        
        return False
        


# Your self object will be instantiated and called as such:
# obj = self(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()