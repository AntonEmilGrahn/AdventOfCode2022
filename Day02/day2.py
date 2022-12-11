#!/usr/bin/env python3

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        parsed_array = []
        for element in raw_array:
            parsed_array.append(element.split(" "))
    return parsed_array

def calculate_score(parsed_array):
    points = {'X': 1, 'Y': 2, 'Z':3}
    outcome = {'XA': 3, 'YA': 6, 'ZA':0,'XB': 0, 'YB': 3, 'ZB':6,'XC': 6, 'YC': 0, 'ZC':3}
    second_outcome = {'X': 0, 'Y': 3, 'Z':6}
    find_play= {'XA': 'Z', 'YA': 'X', 'ZA': 'Y','XB': 'X', 'YB': 'Y', 'ZB': 'Z','XC': 'Y', 'YC': 'Z', 'ZC': 'X'}
    first_score = 0
    second_score = 0
    for game in parsed_array:
        first_score+=outcome[game[1]+game[0]]+points[game[1]]
        second_score+= second_outcome[game[1]]+points[find_play[game[1]+game[0]]]
    return first_score,second_score

if __name__ == "__main__":
    parsed_array = read_data()
    first_score,second_score = calculate_score(parsed_array)
    print("First Score: ",first_score, "Second Score: ",second_score)