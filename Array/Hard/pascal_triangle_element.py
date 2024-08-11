"""

for given row and col print the element from the pascal triangle.

solution: any element of the pascal's triangle is given as (r-1)C(c-1)
where C is the combination.

nCr = n! / ((r!) * (n-r)!)

this can be modified as 

10C3 = 10!/(3! * 7!) === 10*9*8/3*2*1
"""

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascal_element(row, col):
    return nCr(row-1, col-1)

print(pascal_element(6, 2))