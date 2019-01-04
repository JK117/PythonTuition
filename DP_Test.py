
v = [[3], [1, 2], [6, 2, 3], [3, 5, 4, 1]]
m = []

n = 4

for i in range(1, n+1):
    m.append([0] * n)

print(v)
print(m)

for i in range(0, n):
    for j in range(0, i+1):
        print('i: ' + str(i) + ', j: ' + str(j))
        if i == 0:
            m[0][0] = v[i][j]
        elif j == 0:
            m[i][0] = v[i][j] + m[i - 1][0]
        else:
            m[i][j] = v[i][j] + max(m[i - 1][j - 1], m[i - 1][j])
        print(m)


print(max(m[n - 1]))
