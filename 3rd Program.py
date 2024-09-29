def max_of_mins(arr, k):
    n = len(arr)
    if k > n:
        return None  # If k is greater than the length of the array

    max_of_mins = float('-inf')

    for i in range(n - k + 1):
        # Extract the current subarray of length k
        subarray = arr[i:i + k]
        # Find the minimum of the current subarray
        min_value = min(subarray)
        # Update the maximum of minimums
        max_of_mins = max(max_of_mins, min_value)

    return max_of_mins

# Sample Input
x = 1  # Length of segment
n = 5  # Size of space
space = [1, 2, 3, 1, 2]  # Array

# Call the function and print the output
result = max_of_mins(space, x)
print(result)  # Output should be 3
