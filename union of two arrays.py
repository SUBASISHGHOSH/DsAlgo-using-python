# optimal without using extra space
#time complexity o(n*m*mlogn) space complexity 0(1)
def merge(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr2[j] < arr1[i]:
                arr2[j], arr1[i] = arr1[i], arr2[j]
                arr2 = sorted(arr2)
                break
    return arr1, arr2


print(merge([10, 12, 19],
            [11, 18, 20]))
#more optimised order of o(nlogn)
#gap algorithm/shell algo
