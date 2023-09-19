def get_diagonal_sum(mat, i, j, x, y):
    n, m = len(mat), len(mat[0])
    sum = 0
    while 0 <= i < n and 0 <= j < m:
        sum += mat[i][j]
        i += x
        j += y
    
    return sum

n = int(input())
for _ in range(n):
    n, m = list(map(int, input().split()))
    
    matrix = []
    for _ in range(n):
        ls = list(map(int, input().split()))
        matrix.append(ls)
    
    ans = float("-inf")
    for i in range(n):
        for j in range(m):
            temp = 0
            temp += get_diagonal_sum(matrix, i, j, -1, -1)
            temp += get_diagonal_sum(matrix, i, j, -1, 1)
            temp += get_diagonal_sum(matrix, i, j, 1, -1)
            temp += get_diagonal_sum(matrix, i, j, 1, 1)
            
            temp -= 3 * matrix[i][j]
            
            ans = max(ans, temp)
    
    print(ans)
