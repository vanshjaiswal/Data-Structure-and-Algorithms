"""Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i is defined as the sum of all divisors of i."""


"""Solution:

We start with a loop that goes through the numbers from 1 to N, i.e. i takes values from 1 to N.

In each of these iterations, we want to find the maximum integer k that is less than or equal to N/i. This integer k gives us the number of times that i fits into N without exceeding N. That is, if i exactly divides N, then k will be 1, because only once does i fit into N.

For example, if N = 10 and i = 3, then N // i is 3, since 3 fits three times in 10. Thus, k will be 3, i.e. i can be added three times to the sum.

To summarize, the line k = N // i helps to calculate the number of times a number i can be added to the total sum of the divisors. This allows the sum to be calculated without the use of nested loops, and this is the algebraic approach that helps optimize the code."""

import numpy as np
def divisor_sum(N):
    if N <= 0:
        return 0
    div_sum = 0
        
    for i in range(1, N + 1):
        k = N // i
        print(i, N//i, i*k)

        div_sum += i * k

    return div_sum



#driver code
print(divisor_sum(10))


