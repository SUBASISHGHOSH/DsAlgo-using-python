from icecream import ic
def maxSubArraySum(a):
    max_local = max_global = a[0]
    for i in range(1,len(a)):
        max_local = max(a[i], max_local + a[i])
        ic(max_local)
        if max_local > max_global:
            max_global = max_local
    return max_global


print(maxSubArraySum([1, 2, 3, -8, 7]))
