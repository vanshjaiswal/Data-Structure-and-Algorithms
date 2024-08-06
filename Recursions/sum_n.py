def sum_n(N):
    if N==0:
        return 0
    return N + sum_n(N-1)

print(sum_n(3))