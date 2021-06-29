#quick select
#error
arr = [int(input()) for i in range(int(input('length:')))]
k = int(input('k:'))
p = len(arr) - 1
start = 0


def qck(arr, k, p, start):
    slst, blst = [], []
    for i in range(start, p):
        if arr[i] < arr[p]:
            slst.append(arr[i])
        else:
            blst.append(arr[i])
    arr = slst + [arr[p]] + blst
    print(slst,blst,p)
    p = len(slst)
    if (k - 1) < p:
        p = p - 1
        start = 0
        qck(arr, k, p, start)
    elif (k - 1) > p:
        p = len(arr) - 1
        start = len(slst)
        qck(arr, k, p, start)
    elif (k - 1) == p:
        return arr[p]
    if type(qck(arr, k, p, start)) == int:  # as soon as we get the value we come out of the recursion depth
        return qck(arr, k, p, start)


print(qck(arr, k, p, start))
