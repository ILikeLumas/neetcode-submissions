class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.Dynamic = [None] * capacity
        
    def get(self, i: int) -> int:
        return self.Dynamic[i]

    def set(self, i: int, n: int) -> None:
        self.Dynamic[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.Dynamic[self.size] = n
        self.size += 1

    def popback(self) -> int:
        value = self.Dynamic[self.size - 1]
        self.size -= 1
        if self.size != 0:
            self.set(self.size, None)
        return value

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        newArray = [None] * newCapacity
        for i in range(self.size):
            newArray[i] = self.Dynamic[i]
        self.Dynamic = newArray
        self.capacity = newCapacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
