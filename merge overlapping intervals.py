a = [[1, 3], [2, 6], [8, 10], [15, 18]]
a.sort()
b = []
if len(a) > 1:
    for i in range(1, len(a)):
        p = a[i - 1][1]
        if p >= a[i][0]:
            if p <= a[i][1]:
                b.append([a[i - 1][0], a[i][1]])
            elif p > a[i][1]:
                p -= 1
        else:
            b.append(a[i])
    print(b)
else:
    print(a)
