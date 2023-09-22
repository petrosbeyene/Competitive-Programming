n = int(input())
for _ in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    
    i = 0
    sum = 0
    while i < m:
        j = i
        if arr[i] > 0:
            pos_val = float("-inf")
            while j < m and arr[j] > 0:
                pos_val = max(pos_val, arr[j])
                j += 1
            sum += pos_val
            i = j
        else:
            neg_val = float("-inf")
            while j < m and arr[j] < 0:
                neg_val = max(neg_val, arr[j])
                j += 1
            sum += neg_val
            i = j
    
    print(sum)
    
    
