#!/usr/bin/env python3
import numpy as np

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        parsed_array = []
        for element in raw_array:
            parsed_array.append(element.split(" "))
    return parsed_array

def calculate_score(parsed_array):
    points = {'X': 1, 'Y': 2, 'Z':3}

    score = 0
    for game in parsed_array:
        print()
    return score

if __name__ == "__main__":
    parsed_array = read_data()
    score= calculate_score(parsed_array)
    print("Score: ",score)