#!/usr/bin/env python3
import re

def read_data():
    with open('crates.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        crates_array = [[],[],[],[],[],[],[],[],[],[],[]]
        for i,element in enumerate(raw_array[::-1]):
            element.replace('[','').replace(']','').replace(' ','').split(" ")
            if i == 0: pass
            for n, crate in enumerate(element):
                crates_array[n].append(crate)
        print(crates_array)
        
    with open('moves.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        moves_array = []
        for move in raw_array:
            moves_array.append([int(s) for s in re.findall(r'\b\d+\b', move)])
    return moves_array,crates_array

def re_arrange_crates(moves_array,crates_array):
    first_crates = []
    second_score = 0

    return first_crates,second_score

if __name__ == "__main__":
    moves_array,crates_array = read_data()
    first_crates,second_score= re_arrange_crates(moves_array,crates_array)
    print("First Crates: ",first_crates, "Second Score: ", second_score)