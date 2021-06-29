# Given an array nums containing n distinct numbers in the range [0, n], return the only number
# in the range that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
# using HashSet
arr = [0, 1]
h = [0] * (len(arr)+1)
for i in arr:
    h[i] = 1
for j in range(len(h)):
    if h[j] != 1:
        print(j)
