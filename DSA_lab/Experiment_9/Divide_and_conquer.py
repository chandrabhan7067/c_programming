# 9. Find the minimum and maximum element in an array using Divide and Conquer

def findMinAndMax(A, left, right, min, max):
 
    if left == right:               
 
        if min > A[right]:          
            min = A[right]
 
        if max < A[left]:           
            max = A[left]
 
        return min, max
 
 
    if right - left == 1:           
 
        if A[left] < A[right]:      
            if min > A[left]:      
                min = A[left]
 
            if max < A[right]:      
                max = A[right]
 
        else:
            if min > A[right]:      
                min = A[right]
 
            if max < A[left]:       
                max = A[left]
 
        return min, max
 
    mid = (left + right) // 2
 
    min, max = findMinAndMax(A, left, mid, min, max)
    min, max = findMinAndMax(A, mid + 1, right, min, max)
    return min, max
 
 
if __name__ == '__main__':
 
    A = [7, 2, 8, 3, 1, 6, 7, 9, 4]
 
    (min, max) = (A[0],A[0])
    (min, max) = findMinAndMax(A, 0, len(A) - 1, min, max)
 
    print("The minimum element in the list is", min)
    print("The maximum element in the list is", max)