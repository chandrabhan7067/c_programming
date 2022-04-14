def heapify(arr,n,i):
    larges = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[larges] < arr[left]:
        larges = left
    if right<n and arr[larges]<arr[right]:
        larges = right
    if larges != i:
        arr[i],arr[larges] = arr[larges],arr[i]
    heapify(arr,n,larges)

def insert(arr,number):
    size = len(arr)
    if size==0:
        arr.append(number)
    else:
        arr.append(number)
    for i in range ((size//2)-1,-1,-1):
        heapify(arr,size,i)

def deletion(arr,number):
    size = len(arr)
    for i in range(0,size):
        if number == size(i):
            break

    arr[i],arr[size-1] = arr[size-1],arr[i]
    del arr[size-1]

    for i in range((len(arr)//2),-1,-1):
        heapify(arr,len(arr),i)

def rootnode(arr):
    print(arr[0])

arr = [2,5,7,9]
heapify(arr,4,0)
# insert(arr,4)
# insert(arr,3)
print(arr)