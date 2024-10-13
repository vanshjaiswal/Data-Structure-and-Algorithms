"""
How to find if it is a DP problem ?

1: If the question is asking about the count of ways/choices

2: if the question is asking about the minimum or maximum from all the ways.


We have to try to apply the recursion. Then we can convert the recursion into DP.


WAYS to apply the DP technique

Step 1: Try to represent the problems in terms of index

Step 2: Try all the possible choices/ways at every index according to problem statement

Step 3: If the problem states:
        1: Count all the ways : return the sum of choices (return l+r)
         
        f(ind){
        base case: return 1 if True else return 0

        #take
        add.element
        l = f(ind+1)

        #not take
        remove.element
        r = f(ind+1)

        return l+r

        }

        2: Find max/min values: return the choices with max or min values



"""