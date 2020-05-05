#https://www.geeksforgeeks.org/largest-sum-contiguous-increasing-subarray/?ref=rp
#Largest sum contiguous increasing subarray
# Given an array of n positive distinct integers. The problem is to find the largest sum of contiguous increasing subarray in O(n) time complexity.

# Examples :

# Input : arr[] = {2, 1, 4, 7, 3, 6}
# Output : 12
# Contiguous Increasing subarray {1, 4, 7} = 12

# Input : arr[] = {38, 7, 8, 10, 12}
# Output : 38



import sys
def lon(arr):

    result = -sys.maxsize

    for i in range(len(arr)):
        current_sum = arr[i]

        while(i+1< len(arr) and arr[i+1] > arr[i]):
            current_sum = current_sum + arr[i+1]
            i = i + 1

        result = max(result, current_sum)
    return result

print(lon([1, 1, 4, 7, 3, 6]))



