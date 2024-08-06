def print_Nto1(N):
    if N==0:
        return
    print(N, end=" ")
    print_Nto1(N-1)
    

print_Nto1(5)