#!/usr/bin/env python3

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        parsed_array = []
        plain_array = []
        for element in raw_array:
            element = list(element)
            length = len(element)
            plain_array.append(element)
            parsed_array.append([element[0:int(length*0.5)],element[int(length*0.5):]])
        print(plain_array)
    return plain_array,parsed_array

def ascii_scoring(item):
    ascii_code =  int(ord(item))
    if ascii_code>=97: score = ascii_code-96
    if ascii_code<97: score = ascii_code-38
    return score

def calculate_score(parsed_array):
    total_score = 0
    for backpack in parsed_array:
        try:
            for item0 in backpack[0]:
                if item0 in backpack[1]:
                    score = ascii_scoring(item0)
                    total_score+= score
                    raise StopIteration
        except StopIteration: pass
    return total_score

def calculate_badge_score(plain_array):
    badge_score = 0
    for i,backpack in enumerate(plain_array):
        if i% 3 == 0:
            try:
                for item in backpack:
                    if item in plain_array[i+1] and item in plain_array[i+2]:
                        score = ascii_scoring(item)
                        badge_score+= score
                        raise StopIteration
            except StopIteration: pass
    return badge_score

if __name__ == "__main__":
    plain_array,parsed_array = read_data()
    score= calculate_score(parsed_array)
    badge_score= calculate_badge_score(plain_array)
    print("Score: ",score, "Badge Score: ", badge_score)