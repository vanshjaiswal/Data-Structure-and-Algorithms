def print_ntimes(N):
    if N==0:
        return
    print_ntimes(N-1)
    print(N, end=" ")

print_ntimes(10)