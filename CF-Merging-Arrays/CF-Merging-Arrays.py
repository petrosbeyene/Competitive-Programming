n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def mergeSortedArr(arr1, arr2, n, m):
    i, j = 0, 0
    merged = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    if i < n:
        merged.extend(arr1[i:])
    
    if j < m:
        merged.extend(arr2[j:])
    
    return merged

print(*mergeSortedArr(arr1, arr2, n, m))
