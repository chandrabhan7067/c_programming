# class Nood:
#     def __init__(self,item):
#         self.item = item
#         self.next = None

# class Linklist:
#     def __init__(self):
#         self.head = None

#     def details(self):
#         while items.head != None:
#             print(items.head.item,end=' ')

#             items.head = items.head.next

# if __name__ == '__main__':

#     items = Linklist()
#     items.head = Nood(5)
#     second = Nood(4)
#     third = Nood(6)

#     items.head.next = second
#     second.next = third
#     items.details()
#     # while items.head != None:
#     #     print(items.head.item,end=" ")
        

#     #     items.head = items.head.next
        




class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class Linklist:
    def __init__(self):
        self.head = None


    def details(self):
        while self.head != 0:
            print(self.head.data , end=' ')

            self.head = self.head.next

obj = Linklist()

obj.head = node(6)
second = node(7)
third = node(9)
fourth = node(1)

obj.head.next = second
second = third
third = fourth
obj.details()
# obj.details()
# while obj.head != None:
#     print(obj.head.data,end=" ")
              
def delete_element(self,number):
    if self.head is None:
        return 

    
    