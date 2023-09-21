#brute force
n = int(input())
arr = list(map(int, input().split()))

odds = 0
evens = 0
for i in arr:
    if i%2 == 0:
        evens += 1
    else:
        odds += 1

if evens and odds:
    print(*sorted(arr))
else:
    print(*arr)
