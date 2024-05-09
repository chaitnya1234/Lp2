
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = input("Enter a sorted array of numbers separated by spaces: ").split()
arr = [int(x) for x in arr]


target = int(input("Enter the target value: "))


result = binary_search(arr, target)


if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
