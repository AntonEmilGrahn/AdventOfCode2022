#!/usr/bin/env python3
from collections import Counter
def read_data():
    with open('data.txt', 'r') as f:
        parsed_array = list(f.read())
    return parsed_array

def check_for_marker(parsed_array,number_of_characters):
    for i,_ in enumerate(parsed_array):
        if (i>number_of_characters-1) and len([item for item, count in Counter(parsed_array[i-number_of_characters:i]).items() if count > 1]) == 0: 
            score = i
            break
    return score
    
if __name__ == "__main__":
    parsed_array = read_data()
    first_score = check_for_marker(parsed_array,4)
    second_score = check_for_marker(parsed_array,14)
    print("First Score: ",first_score, "Second Score: ", second_score)