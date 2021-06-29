# dutch flag algo
arr = [1, 0, 2, 0, 1]
low, mid = 0, 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] < 1:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[high], arr[mid] = arr[mid], arr[high]
        high -= 1

print(arr)
