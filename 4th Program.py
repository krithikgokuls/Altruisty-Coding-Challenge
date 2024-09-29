def find_odd_balloon_color(n, balloons):
    # Dictionary to count occurrences of each color
    count_dict = {}
    
    # Count occurrences of each balloon color
    for color in balloons:
        if color in count_dict:
            count_dict[color] += 1
        else:
            count_dict[color] = 1
            
    # Find the first color with an odd count
    for color in balloons:
        if count_dict[color] % 2 == 1:
            return f"{color} -> '{color}' colour balloon is present odd number of times in the bunch."
    
    return "All are even"

# Sample Inputs
# Example 1
n1 = 7
balloons1 = ['r', 'g', 'b', 'b', 'g', 'y', 'y']
output1 = find_odd_balloon_color(n1, balloons1)
print(output1)

# Example 2
n2 = 10
balloons2 = ['a', 'b', 'b', 'b', 'c', 'c', 'c', 'a', 'f', 'c']
output2 = find_odd_balloon_color(n2, balloons2)
print(output2)
