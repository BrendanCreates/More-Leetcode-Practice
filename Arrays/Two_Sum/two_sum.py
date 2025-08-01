"""

Two Sum

Description: Given array of integer nums and integer target return the indeces of two numbers such that they add up to target

Constraits: There is always exactly one solution, can not use the same number twice, can return the numbers in any order, 2 <= nums.length <= 10^4, target and nums can be negative

"""

"""

Approaches: 

First idea that came to mind is to sort in ascending order, with a pointer on the first index and a second pointer on the second index, then moving the right index to increase the sum when the sum is below the target and when the sum is too large we move the left pointer, if we need to move the left pointer and the right pointer is right beside it they move together, I'm thinking of a different approach because this is nlogn

possibly starting the pointers at the opposite ends makes it slightly more efficient

Studying the best solution: the best approach to this problem is to use a hash map that stores the difference of the current element in the array and the target and moving along doing this until the difference is a value in the hashmap and we return that and the current index in the array

"""

def two_sum(arr, target):
    visited_i = {}
    for i in range(len(arr)):
        if (target - arr[i]) in visited_i: # not going to use the get function because when it returns index 0 the condition will be considered false
            return [i, visited_i[target - arr[i]]]
        visited_i[arr[i]] = i

def main():
    arr = [2, 11, 7, 15]
    target = 9
    print(two_sum(arr, target))

if __name__ == "__main__":
    main()