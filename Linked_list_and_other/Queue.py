class Queue:
    def __init__(self):
        self.item = []
        
    def Push(self,data):
        self.item.append(data)
        # print(self.item)

    def Pop(self):
        if self.item == []:
            print('The queue is empty')
        else:
            self.item.pop(0)
        # print(self.item)

    def Peek_element(self):
        if self.item == []:
            print('list is Empty')
        else:
            return self.item[-1]
            
ob = Queue()
ob.Push(7)
ob.Push(3)
ob.Push(4)
print(ob.item)
ob.Pop()
print(ob.Peek_element())
print(ob.item)


