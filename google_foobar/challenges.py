def find_triple_dp(x):
    cnt = 0
    array_len = len(x)
    divide = [0] * array_len
    for i in range(1, array_len - 1):
        for j in range(i + 1, array_len):
            if x[j] % x[i] == 0:
                divide[i] += 1
    for i in range(array_len - 1):
        for j in range(i + 1, array_len):
            if x[j] % x[i] == 0:
                cnt += divide[j]
    return cnt
    
def grandest_of_them_all(n):
    f = [
            [1 if i == 1 and j > 0 and i > 0 else 0 for i in range(n+1)]
            for j in range(n+1)
    ]
    for j in range(2, n + 1):
        for i in range(2, n + 1):
            _x = i
            while _x - j > 0:
                f[i][j] += f[_x - j][j - 1]
                _x = _x - j
    return sum(f[n][2:])
