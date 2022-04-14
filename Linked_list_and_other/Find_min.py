# arr = [5,3,2,6,3,1,2,5]
# minimum = arr[0]
# for i in range(len(arr)):
#     if arr[i]<minimum:
#         minimum = arr[i]
    
# print(minimum)

def Divide(arr,mid,low,high):
    i = low
    j = mid
    
    minimum = arr[low]
    for i in range(low,mid):
        if arr[i]<minimum:
            minimum = arr[i]

    minimum2 = arr[mid+1]
    for j in range(mid+1,high):
        if arr[i]<minimum2:
            minimum2 = arr[i]

    if minimum<minimum2:
        print('our minimum is',minimum)
    else:
        print('our minimum is',minimum2)


def find_minimum(arr,low,high):
    if low<high:
        mid = low+high//2
        find_minimum(arr,low,mid)
        find_minimum(arr,mid+1,high)
        Divide(arr,mid,low,high)


arr = [2,4,3,1,5,7,5,0]
n = len(arr)
print(arr)
find_minimum(arr,0,n)
print(arr)
        