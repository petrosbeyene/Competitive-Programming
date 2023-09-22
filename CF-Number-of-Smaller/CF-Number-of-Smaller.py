n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def numberOfSmaller(arr1, arr2, n, m):
    i, j =  n-1, m-1
    ans = [0]*m
    while i >= 0 and j >= 0:
        if arr1[i] < arr2[j]:
            ans[j] = i + 1
            j -= 1
        else:
            i -= 1
    
    return ans

print(*numberOfSmaller(arr1, arr2, n, m))
        
