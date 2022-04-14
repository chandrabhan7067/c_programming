# Function to heapify the tree
# def heapify(arr, n, i):
#     # Find the largest among root, left child and right child
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     #print("print l r",l,r)
#     if l < n and arr[i] < arr[l]:
#         #print("left node",arr[l])
#         largest = l

#     if r < n and arr[largest] < arr[r]:
#         #print("right node",arr[r])
#         largest = r

#     # Swap and continue heapifying if root is not largest
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)


# # Function to insert an element into the tree
# def insert(array, newNum):
#     size = len(array)+1
#     # if size == 0:
#     array.append(newNum)
#     # else:
#     #     array.append(newNum)
#     for i in range((size // 2) - 1, -1, -1):
#             heapify(array, size, i)


# arr = []

# insert(arr, 3)
# insert(arr, 4)
# insert(arr, 9)
# insert(arr, 5)
# insert(arr, 2)
# print("max heap",arr)



def heapify(arr, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[i] < arr[right]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def insert(arr, number):
    size = len(arr)
    arr.append(number)
    for i in range((size // 2) - 1, -1, -1):
        heapify(arr, size, i)


arr = []
insert(arr, 4)
insert(arr, 1)
insert(arr, 3)
insert(arr, 3)
print(arr)
