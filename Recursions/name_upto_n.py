def name_upto_n(N):
    if N==0:
        return
    name_upto_n(N-1)
    print("Vansh")

name_upto_n(5)