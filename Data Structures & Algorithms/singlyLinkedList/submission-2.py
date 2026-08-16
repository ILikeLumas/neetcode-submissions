class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size or i < 0:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def insertHead(self, val: int) -> None:

        new = Node(val)

        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new
        
        self.size += 1

    def insertTail(self, val: int) -> None:
        
        new = Node(val)

        if self.size == 0:
            self.tail = new
            self.head = new
        else:
            self.tail.next = new
            self.tail = new
            
        self.size += 1

    def remove(self, index: int) -> bool:
        
        curr = self.head
        
        if index < 0 or index >= self.size:
            return False
        elif index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif index == self.size - 1:
            for _ in range(index - 1):
                curr = curr.next
            self.tail = curr
            curr.next = None
        else:
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        
        self.size -= 1

        return True
            

    def getValues(self) -> List[int]:
        curr = self.head
        ans = []
        for i in range(self.size):
            ans.append(curr.value)
            curr = curr.next
        return ans
        
