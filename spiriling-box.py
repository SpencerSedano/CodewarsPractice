def fill_2d_list(m, n):
    
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):

            distance_to_boundary = min(i, j, n - i - 1, m - j - 1)


            value_to_fill = distance_to_boundary + 1


            result[i][j] = value_to_fill

    return result

#Example
m = 5
n = 8
result = fill_2d_list(m, n)
for row in result:
    print(row)
