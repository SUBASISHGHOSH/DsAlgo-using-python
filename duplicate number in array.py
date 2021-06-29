# # using hash table
# num = [1, 3, 4, 1, 2]
# hash = [0] * len(num)
# for i in range(len(num)):
#     hash[num[i]] = hash[num[i]] + 1
# # print(hash)
# for i in range(len(hash)):
#     if hash[i] == 2:
#         print(i)

# using flyod's turtle hare method
num = [1, 2, 4, 3, 5, 2, 2]
turtle, hare = 0, 0
# hare moves by 2
# turtle moves by 1
while True:
    turtle = num[turtle]
    hare = num[num[hare]]
    if turtle == hare:  # first collision
        break
hare=0
while True:
    # both pointer moves by 1
    turtle = num[turtle]
    hare = num[hare]
    if turtle == hare:  # second collision
        break
print(turtle)
