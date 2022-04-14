def bubble(a):
    n = len(a)
    # for i in range(n-1):
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

def Alternative(arr):
    n = len(arr)
    # arr.sort()
    bubble(arr)
    i = 0
    j = n-1

    while(i<j):
        print(arr[i],end=' ')
        i+=1
        print(arr[j],end=' ')
        j-=1
        
    if(n%2 != 0):
        print(arr[i])
        
        
arr = [5,3,6,7,8,9]
# print(arr)
Alternative(arr)
# print(arr)
