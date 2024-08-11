"""
For a give N print the entire row of the pascal triangle


"""

#Brute force

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascal_row(N):
    for i in range(1,N+1):
        print(nCr(N-1, i-1))

# pascal_row(6)

#Optimal

"""
If you assign the index to each element of the pascal triangle row.

then every element can be calculated as 

ans * (row-col)/col

https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/

"""

def pascal_row_opt(N):
    res= [1]
    ans = 1
    for i in range(1, N):
        ans = ans*(N-i)
        ans = ans//i
        res.append(ans)
    return res
    
print(pascal_row_opt(6))


"""
Print entire pascal triangle having N rows

"""

def pascalTriangle(N):
    ans=[]
    for i in range(1,N+1):
        temp=pascal_row_opt(i)
        ans.append(temp)
    return ans

print(pascalTriangle(6))

