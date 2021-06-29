arr = [0, 1, 3, 3, 4, 5]
ran = len(arr)
cr_arr = [i for i in range(ran)]


def doXor(arr):
    temp = arr[0] ^ arr[1]
    for i in range(2, len(arr)):
        temp ^= arr[i]
    return temp


initialXor = doXor(arr + cr_arr)
# finding most significant bit to right
initialXor = list(bin(initialXor))
rmBit = -1
while True:
    if initialXor[rmBit] == '1':
        break
    rmBit -= 1
# segregating to buckets
bucket1, bucket2 = [], []
arr = arr + cr_arr
for i in range(len(arr)):
    if bin(arr[i])[rmBit] == '1':
        bucket1.append(arr[i])
    else:
        bucket2.append(arr[i])

# XOR bucket 1s & 2s elements
print(doXor(bucket1), doXor(bucket2))
