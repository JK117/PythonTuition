
n = int(input())
m = int(input())
cx = int(input())
cy = int(input())

mark_array = [[0 for col in range(m+1)] for raw in range(n+1)]

x = [1,1,2,2,-1,-1,-2,-2]
y = [2,-2,1,-1,2,-2,1,-1]

mark_array[cx][cy] = 1
for i in range(8):
    tx = cx + x[i]
    ty = cy + y[i]
    if 0 <= tx <= n and 0 <= ty <= m:
        mark_array[tx][ty] = 1

result_array = [[0 for col in range(m+1)] for raw in range(n+1)]
result_array[0][0] = 1
for i in range(n+1):
    for j in range(m+1):
        if i:
            if not mark_array[i][j]:
                result_array[i][j] += result_array[i-1][j]
        if j:
            if not mark_array[i][j]:
                result_array[i][j] += result_array[i][j-1]

print(result_array[n][m])
print(mark_array)
print(result_array)