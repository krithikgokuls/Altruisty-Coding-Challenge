def count_frogs_between_stones(s, start_indices, end_indices):
    results = []
    
    for start, end in zip(start_indices, end_indices):
        # Extract the substring from start to end
        substring = s[start-1:end]  # Convert 1-indexed to 0-indexed
        # Count the number of frogs ('*') between the two stones ('|')
        first_bar = substring.find('|')
        last_bar = substring.rfind('|')

        # If we have at least two bars, count the frogs between them
        if first_bar != -1 and last_bar != -1 and first_bar != last_bar:
            # The substring between the first and last bar
            count_frogs = substring[first_bar:last_bar].count('*')
        else:
            count_frogs = 0
            
        results.append(count_frogs)
    
    return results

# Sample input for custom testing
s = "*|*|"
start_indices = [1]
end_indices = [3]

# Function call
output = count_frogs_between_stones(s, start_indices, end_indices)
print(output)  # Output: [0]
