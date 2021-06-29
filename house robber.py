
arr = [7, 2, 4, 9, 3]


def robber(arr, n=5):
    if n==0:
        return 0
    elif n==1:
        return arr[0]
    elif n != 1:
        return (max(robber(arr, n - 1), (arr[n - 1] + robber(arr, n - 2))))



print(robber(arr, 5))
