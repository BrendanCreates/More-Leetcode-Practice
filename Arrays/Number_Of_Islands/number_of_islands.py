"""

Duplicate Values

Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

Constraints: 1 <= nums.length <= 10^5, -10^9 <= nums[i] <= 10^9

"""

"""

Approaches: 

Maybe do a hashmap

if we are allowed to use basic python functions we can make a set out of the array and grab the length of the list - fastest approach

without using python trickery another way is to order the list then slide a 2 element window

"""