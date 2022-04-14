def Heapify(arr,n,i):
    largest = i
    left = i*2+1
    right = i*2+2

    #let's compare the parent to his chiled
    #min heap
    if left<n and arr[left]<arr[largest]:
        largest = left
    
    if right<n and arr[right]<arr[largest]:
        largest = right

    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        Heapify(arr,n,largest)

def Insert_value(arr,value):
    #Insert the element at the last
    size = len(arr)+1
    arr.append(value)
    for i in range((size//2)-1,-1,-1):
        Heapify(arr,size,i)

def Delete_Element(arr,value):
    # Delete element that user will give
    size = len(arr)
    for i in range(0,size):
        if value == arr[i]:
            arr[i],arr[size-1] = arr[size-1],arr[i]
            del arr[size-1]
            size = len(arr)
            for i in range((size//2)-1,-1,-1):
                Heapify(arr,size,i)
            print('After delete',arr)
            break
    else:
        print('the value not in array')

def Root_node(arr):
    print(arr[0])

arr = []
Insert_value(arr,4)
Insert_value(arr,3)
Insert_value(arr,6)
print('The array is ',arr)
Delete_Element(arr,5)
# print('After the delete elemnet the array is ',arr)
print('Root node is ')
Root_node(arr)
