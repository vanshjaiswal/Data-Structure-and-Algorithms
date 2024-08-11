"""
You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

Example 2:
Input Format
: array[] = {3,1,2,5,4,6,7,5}
Result
: {5,8)
Explanation
: A = 5 , B = 8 
Since 5 is appearing twice and 8 is missing

"""

def repeating_missing(arr):
    dic = dict(zip(set(arr), [0]*len(set(arr))))
    N=len(arr)
    for i in arr:
        dic[i]+=1
    key_list=list(dic.keys())
    value_list=list(dic.values())
    duplicate_index = value_list.index(2)
    duplicate_value = key_list[duplicate_index]

    arr.remove(duplicate_value)
    missing = (N*(N+1))/2-sum(arr)
    return duplicate_value, int(missing)

# print(repeating_missing([3,1,2,5,4,6,7,5]))

#Optimal 1 using algebra

"""
https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/

he idea is to convert the given problem into mathematical equations. Since we have two variables i.e. missing and repeating, we will try to form two linear equations. And then we will find the values of two variables using those equations.

Assume the repeating number to be X and the missing number to be Y.

In the array, the numbers are between 1 to N, and in that range, one number is missing and one number is occurring twice.

Step 1: Form equation 1:

Now, we know the summation of the first N numbers is:
Sn = (N*(N+1))/2

S = the summation of all the elements in the given array.

S - Sn = X - Y…………………equation 1

Form equation 2: summation of squares of the first N numbers is:
S2n = (N*(N+1)*(2N+1))/6

S2 = the summation of squares of all the elements in the given array.

S2-S2n = X2-Y2. equation 2

X+Y = (S2 - S2n) / (X-Y) equation 3

substitue and find X and Y from X+Y and X-Y

"""

def repeating_missing_algebra(arr):
    N = len(arr)
    Sn = (N*(N+1))/2
    Sn2 = (N*(N+1)*(2*N+1))/6
    S=0
    S2=0
    for i in range(N):
        S += arr[i]
        S2 += arr[i] * arr[i]

     # S-Sn = X-Y:
    val1 = S - Sn

    # S2-S2n = X^2-Y^2:
    val2 = S2 - Sn2

    # Find X+Y = (X^2-Y^2)/(X-Y):
    val2 = val2 // val1

    # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
    # Here, X-Y = val1 and X+Y = val2:
    x = (val1 + val2) // 2
    y = x - val1

    return int(x), int(y)

print(repeating_missing_algebra([3,1,2,5,4,6,7,5]))
