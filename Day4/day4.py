#!/usr/bin/env python3

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        parsed_array = []
        for element in raw_array:
            element = element.split(",")
            first_range = element[0].split("-")
            if first_range[0]==first_range[1]: first_range= {int(first_range[0])}
            else: first_range = set(range(int(first_range[0]),int(first_range[1])+1))
            second_range = element[1].split("-")
            if second_range[0]==second_range[1]: second_range= {int(second_range[0])}
            else: second_range = set(range(int(second_range[0]),int(second_range[1])+1))  
            parsed_array.append([first_range,second_range])
    return parsed_array

def calculate_score(parsed_array):
    first_score,second_score = 0,0
    for pair in parsed_array:
        if bool(pair[0] & pair[1]): 
            second_score+=1
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]): 
            first_score+= 1
    return first_score,second_score

if __name__ == "__main__":
    parsed_array = read_data()
    first_score,second_score= calculate_score(parsed_array)
    print("First Score: ",first_score, "Second Score: ", second_score)