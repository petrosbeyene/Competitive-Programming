import math
n = int(input())
for i in range(n):
    curr = int(input())
    if curr == 1:
        print(3)
    elif curr%2 != 0:
        print(1)
    else:
        if math.log2(curr) == math.ceil(math.log2(curr)):
            print(curr+1)
        else:
            print(curr - (curr&(curr-1)))
