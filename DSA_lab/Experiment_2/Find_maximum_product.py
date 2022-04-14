# 2. Find maximum product of two integers in an array.

def maxproduct(arr, n):
    if n < 2:
        print("no pair")
        return
    a = arr[0]
    b = arr[1]
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] * arr[j] > a * b:
                a = arr[i]
                b = arr[j]
                print(f"Max product pair is {a,b}")

arr = [16, 14, 8, 7, 15, 2]
n = len(arr)
maxproduct(arr, n)
