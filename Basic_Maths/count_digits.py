"""Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

Input: n = 12
Output: 2
Explanation: 1, 2 when both divide 12 leaves remainder 0.

Input: n = 2446
Output: 1
Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not."""

def count_digits(N):
    count=0
    M=N
    while N>0:
        num = N%10
        if num !=0:
            if M%num == 0:
                count +=1
            N=N//10
    return count

#driver code
print(count_digits(12))
print(count_digits(2446))

