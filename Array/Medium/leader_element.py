"""
Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

Example 1:
Input:

arr = [4, 7, 1, 0]
Output:

7 1 0
Explanation:

Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

arr = [10, 22, 12, 3, 0, 6]
22 12 6


n the above approach, we do a fresh traversal for each candidate. If we think carefully, we only want to compare the elements on the right side. So, what if we start from the last element?
That is, we'll try to remember the greatest element encountered so far and we'll use that to decide whether a candidate is a leader or not.
First, we'll start the traversal from the right. Then, we move toward the left. Whenever we encounter a new element, we check with the greatest element obtained so far.
If the current element is greater than the greatest so far, then the current element is one of the leaders and we update the greatest element.
Else, we proceed with the further elements on the left. This method prints the leaders in the reverse direction of their occurrences. If we are concerned about the order, we can use an extra array or a string to order.

"""

def leader_element(nums):
    n=len(nums)
    max_element = nums[n-1]
    leader=[nums[n-1]]
    for i in range(n-2,-1, -1):
        if nums[i]>max_element:
            leader.append(nums[i])
            max_element = nums[i]
        
    return leader[::-1]

print(leader_element([10, 22, 12, 3, 0, 6]))



