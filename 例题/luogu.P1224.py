import random

def read_ints():
    return list(map(int, input().split()))

def matrix_multiply(A, B, mod):
    n, m, p = len(A), len(A[0]), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def solve_sub2(n, m, k, A):
    B = [[A[i][j] for i in range(n)] for j in range(m)]

    for _ in range(10):
        R = [[random.randint(0, 1)] for _ in range(n)]
        sum_R = sum(r[0] for r in R) % 2

        BR = matrix_multiply(B, R, k)
        ABR = matrix_multiply(A, BR, k)

        for i in range(n):
            if ABR[i][0] != sum_R:
                for j in range(n):
                    if i != j:
                        s = sum(A[i][k] * A[j][k] for k in range(m)) % 2
                        if s == 0:
                            return min(i+1, j+1), max(i+1, j+1)
    return -1, -1

def solve_sub3(n, m, k, A):
    B = [[A[i][j] for i in range(n)] for j in range(m)]

    for _ in range(10):
        R = [[random.randint(0, 2) for _ in range(m)] for _ in range(n)]
        sum_R = sum(sum(row) for row in R) % 3

        BR = matrix_multiply(B, R, k)
        
        for i in range(n):
            s = sum(A[i][j] * BR[j][k] * A[i][k] for j in range(m) for k in range(m)) % 3
            if s != sum_R:
                for j in range(n):
                    if i != j:
                        tmp = sum(A[i][k] * A[j][k] for k in range(m)) % 3
                        if tmp == 0:
                            return min(i+1, j+1), max(i+1, j+1)
    return -1, -1

def main():
    n, m, k = read_ints()
    A = [read_ints() for _ in range(n)]
    
    if k == 2:
        result = solve_sub2(n, m, k, A)
    else:
        result = solve_sub3(n, m, k, A)
    
    print(f"{result[0]} {result[1]}")

main()