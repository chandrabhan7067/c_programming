def Insertion(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]      #value
        j = i-1         #index 
        while(A[j]>key and j>=0):
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

arr = [4,2,7,0,3,1]
print(arr)
Insertion(arr)
print(arr)



# def insertion(a):
#     n = len(a)
#     for i in range(1,n):
#         j = i-1
#         key = a[i]
#         while(key<a[j] and j>=0):
#             a[j+1],a[j] = a[j],a[j+1]
#             # a[j+1] = a[j]
#             j-=1
#         a[j+1] = key
# arr = [131,40,31,29,25,19]
# print(arr)
#insertion(arr)
# print(arr)


