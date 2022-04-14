class Stack:
    def __init__(self):
        self.item = []

    def push(self,data):
        #Element add in the last
        self.item.append(data)
        print(self.item)

    def IsAmpty(self):
        if self.item:
            return False
        else:
            return True
            
    def Pop(self):
        #This fuction pop last element in the list
        if self.item == []:
            print('The stack is Empty')
        else:
            self.item.pop()            
        print(self.item)

    def Peek(self):
        # This fuction return the last Element of he stack
        if self.item:
            return self.item[-1]
        else:
            return None

ob = Stack()
ob.push(6)
ob.push(3)
ob.push(4)
ob.push(7)
ob.Pop()
print(ob.Peek())
print(ob.IsAmpty())
        