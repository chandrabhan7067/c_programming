arr = [2,5,1,3]
value = 6
i = 0
n = len(arr)

while i<n:
    if arr[i] == value:
            # print('yes')
        arr[i],arr[n-1] = arr[n-1],arr[i]
        del arr[n-1]
        # size = len(arr)
        # for i in range((size//2)-1,-1,-1):
        #     Heapify(arr,size,i)
        print('our array after delete the element ',arr)
        break
    i += 1
else:
    print('No change in array because the value that you give is not present in array',arr)


#using for loop

# for i in range(n):
#     if arr[i] == value:
#         print('yes')
#         arr[i],arr[n-1] = arr[n-1],arr[i]
#         del arr[n-1]
#         # size = len(arr)
#         # for i in range((size//2)-1,-1,-1):
#         #     Heapify(arr,size,i)
#         print(arr)
#         break
# else:
#     print('not in arr')