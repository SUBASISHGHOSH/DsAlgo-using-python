def reverse(arr):
    l = len(arr)
    start = 0
    end = l - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


print(reverse(['a', 'b', 'c', 'd', 'e']))

#recursion
# arr = [1, 2, 3, 4, 5]
# start = 0
# end = len(arr) - 1
#
#
# def reverse(arr, start, end):
#     if start >= end:
#         print(arr)
#     else:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#         reverse(arr, start, end)
#
#
# reverse(arr, start, end)