t = int(input())
for i in range(t):
    l = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] <= 1:
            l -= 1
    
    if l > 1:
        print("NO")
    else:
        print("YES")
