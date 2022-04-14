def bubble(a):
    n = len(a)
    # for i in range(n-1):
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

a = [5,0,1,9,2,3,6,8]
print(a)
bubble(a)
print(a)






# def bubble_sort(A):
#     n = len(A)
#     for i in range(n):
#         for j in range(n-i-1):
#             if A[j] > A[j+1]:
#                 A[j],A[j+1] = A[j+1],A[j]


# arr = [3,4,1,2,7,8]
# print(arr)
# print(bubble_sort(arr))
# print(arr)



# def bubble(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(n-i-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
# arr = [0,4,1,2,7,0]
# print(arr)
# print(bubble(arr))
# print(arr)




# def bublle(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(n-1-i):
#            if a[j] > a[j+1]:
#                 a[j] ,a[j+1] = a[j+1],a[j]
                

# a = [63,4,432,21,34,2]
# print(a)
# bublle(a)
# print(a)
