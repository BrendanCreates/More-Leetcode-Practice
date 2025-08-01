"""

Missing Number

Description: Given an array nums containing n distint numbers inthe range [0,n], return the only number in the range that is missing from the array.

Constraints: n == nums.length, 1 <= n <= 10^4, one more i cant see

"""

"""

Approaches:

Use sum of n integers formula to find the missing value -- fastest

"""

def missing_number(arr):
    n = len(arr)
    n_sum = n*(n+1)/2
    arr_sum = sum(arr)
    return n_sum - arr_sum

def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
    print(missing_number(arr))

if __name__ == "__main__":
    main()
