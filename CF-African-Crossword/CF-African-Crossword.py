n, m = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(input()))

rows_dict = {i: {} for i in range(n)}
cols_dict = {j: {} for j in range(m)}

for i in range(n):
    for j in range(m):
        c = grid[i][j]
        if c in rows_dict[i]:
            rows_dict[i][c] += 1
        else:
            rows_dict[i][c] = 1
        
        if c in cols_dict[j]:
            cols_dict[j][c] += 1
        else:
            cols_dict[j][c] = 1

ans = []
for i in range(n):
    for j in range(m):
        c = grid[i][j]
        if rows_dict[i][c] == 1 and cols_dict[j][c] == 1:
            ans.append(c)

dec_ans = "".join(ans)
print(dec_ans)
