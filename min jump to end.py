#not complete
from functools import lru_cache

arr = [1, 3, 6, 1, 5, 3, 4, 5, 1, 5]
i = 0


@lru_cache(maxsize=1000)
def jump(i):
    if (arr[i] + i) >= (len(arr) - 1):
        print(1)
        exit()
    elif arr[i] == 0:
        print(-1)
        exit()
    else:
        for j in range((i + 1), (arr[i] + i + 1)):
            # print(j)
            jump(j)


jump(i)
