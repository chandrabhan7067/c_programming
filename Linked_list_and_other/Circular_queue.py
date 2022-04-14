class Queue:
    def __init__(self,size):
        self.size = size
        self.teal =-1
        self.head = -1
        self.quebe = [0]*size


    def is_Empty(self):
        if self.head == -1 and self.teal== -1:
            return True
        return False

    def is_full(self):
        if self.head < self.teal:
           if self.teal +1 - self.head == self.size:
                return True
        elif self.teal<self.head:
           if self.head+1+self.teal == self.size:
            # if (self.head - self.teal)*self.size == self.size:
                return True
        else:
            return False

    def dequeue(self):
        if not self.is_Empty():
            temp = self.quebe[self.head]
            self.head = (self.size+self.head+1)%self.size
            self.quebe[self.head]
            return temp
        else:
            print('EMPTY')


    def inqueue(self,value):
        if not self.is_full():
            if self.head == -1 and self.teal == -1:
                self.head = self.teal = 0
                self.quebe[self.teal] = value
            
            self.teal = (self.size+self.teal+1)%self.size
            self.quebe[self.teal] = value
            
        else:
            print('full')
            
    def printQueue(self):
        if self.head<self.teal:
            for i in range(self.head,self.teal+1):
               print(self.quebe[i])
        else:
            for i in range(self.head,self.size):
                print(self.quebe[i])
            for i in range(0,self.teal+1):
                print(self.quebe[i])

op = Queue(3)
print(op.is_Empty())
op.inqueue(5)
# op.inqueue(3)
# op.inqueue(6)
# op.inqueue(10)

print(op.is_full())
op.printQueue()
print()
# print(op.is_full())
# print(op.is_Empty())
op.dequeue()
# op.inqueue(10)
# print('dequeqe-------------------------------------------------')
# print(op.is_full())
op.printQueue()
# op.inqueue(12)
# print('dequeqe-------------------------------------------------')
# op.printQueue()