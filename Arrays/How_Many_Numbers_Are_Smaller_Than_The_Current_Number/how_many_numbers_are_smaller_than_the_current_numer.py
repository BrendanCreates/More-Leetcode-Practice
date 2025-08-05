"""

How many numbers are smaller than the current number

Description: Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of j's that are not i and their corresponding value is less than the one corresponding to i, return the result in an array

Constraints: 

"""

"""

Approach:

Maybe make a minheap and the number of children of each parent, this is a less than favorable approach

I'm going to look at my own array example to figure out an approach

5 4 2 5 7 2 7 1 5 8

4 3 1 4 7 1 7 0 4 9

first thing im noticing is if the number is already there i can duplicate

maybe if i used a hash table and create an element for each unique visited element, nah

what if i made an array of length of the set of the array to eliminate duplicates, then i get the frequency of each element, then I add to the right

5 4 2 5 7 2 7 1 5 8
1 2 2 4 5 5 5 7 7 8
1 2 4 5 7 8 -> 
1 2 1 3 2 1 -> 
0 1 3 4 7 9 -> this answer is correct

so basically this approach gets the frequencies of each element and adds the frequencies of all previous elements excluding itself, make a frequency dictionary and do it

"""

from collections import defaultdict

def how_many(arr):
    freq = defaultdict(int)
    for i in range(len(arr)):
        freq[arr[i]] += 1
    
    unique_sorted_nums = sorted(freq.keys())

    smaller_counts = {}
    cumulative_count = 0 # current number of values processed
    for num in unique_sorted_nums:
        smaller_counts[num] = cumulative_count
        cumulative_count += freq[num]

    result = [smaller_counts[x] for x in arr]
    return result

def main():
    my_array = [5, 4, 2, 5, 7, 2, 7, 1, 5, 8]
    output_array = how_many(my_array)
    
    print(f"Input:  {my_array}")
    print(f"Output: {output_array}")

if __name__ == "__main__":
    main()
