def get_oxygen_levels(predefined_values):
    oxygen_levels = []
    
    index = 0
    for round_num in range(1, 4):  # For 3 rounds
        for trainee_num in range(1, 4):  # For 3 trainees
            value = predefined_values[index]
            index += 1
            
            if 1 <= value <= 100:
                oxygen_levels.append(value)
            else:
                print("INVALID INPUT")
                return []  # Return empty list on invalid input
    
    return oxygen_levels

def calculate_average(oxygen_levels):
    averages = []
    
    for i in range(0, len(oxygen_levels), 3):
        average = sum(oxygen_levels[i:i + 3]) / 3
        averages.append(round(average))  # Round the average to the nearest integer
    
    return averages

def find_most_fit(averages):
    max_average = max(averages)
    
    if max_average < 70:
        print("All trainees are unfit. Average Oxygen Values should be rounded.")
        return []
    
    most_fit_trainees = [i + 1 for i, avg in enumerate(averages) if avg == max_average]
    
    return most_fit_trainees, max_average

def main():
    # Replace the list below with the test oxygen values
    predefined_values = [95, 92, 95, 92, 90, 92, 90, 92, 90]
    
    oxygen_levels = get_oxygen_levels(predefined_values)
    if not oxygen_levels:
        return  # Stop if there's an invalid input
    
    averages = calculate_average(oxygen_levels)
    most_fit_trainees, max_average = find_most_fit(averages)
    
    if most_fit_trainees:
        for trainee in most_fit_trainees:
            print(f"Trainee Number : {trainee}")
        print(f"Highest Average Oxygen Level: {max_average}")
        
if __name__ == "__main__":
    main()
