# Find a pair with the given sum in an array.

def find_pair(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                print("Pair is found ", (arr[i], arr[j]))
                return
    print("Pair is not found")


if __name__ == "__main__":

    nums = [8, 7, 2, 5, 3, 1]
    target = 100

    find_pair(nums, target)
