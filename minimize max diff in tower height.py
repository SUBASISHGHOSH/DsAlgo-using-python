def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n - 1] - arr[0]
    small, big = 0, 0

    left = arr[0] + k
    right = arr[-1] - k

    for i in range(1, n):
        small = min(left, arr[i] - k)
        big = max(arr[i - 1] + k, right)
        ans = min(ans, big - small)

    return ans


arr = [8, 1, 5, 4, 7, 5, 7, 9, 4, 6]
k = 10
print(getMinDiff(arr, len(arr), k))
