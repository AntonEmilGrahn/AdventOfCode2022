#!/usr/bin/env python3
import re
def read_data():
    crates_array_input = [['D','T','W','N','L'],['H','P','C'],['J','M','G','D','N','H','P','W'],['L','Q','T','N','S','W','C'],['N','C','H','P'],['B','Q','W','M','D','N','H','T'],['L','S','G','J','R','B','M'],['T','R','B','V','G','W','N','Z'],['L','P','N','D','G','W']]
    with open('moves.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        moves_array_input = []
        for move in raw_array:
            moves_array_input.append([int(s) for s in re.findall(r'\b\d+\b', move)])
    return moves_array_input,crates_array_input

def re_arrange_first_crates(m_array,c_array):
    first_crates = ''
    for move in m_array:
        for _ in range(move[0]):
            c_array[move[2]-1].insert(0,c_array[move[1]-1].pop(0))
    for stack in c_array: first_crates+=stack[0]
    return first_crates

def re_arrange_second_crates(m_array,c_array):
    second_crates = ''
    for move in m_array:
        c_array[move[2]-1]= c_array[move[1]-1][0:(move[0])]+ c_array[move[2]-1]
        del c_array[move[1]-1][0:move[0]]
    for stack in c_array: second_crates+=stack[0]
    return second_crates

if __name__ == "__main__":
    moves_array,crates_array = read_data()
    first_crates = re_arrange_first_crates(moves_array,crates_array)
    moves_array,crates_array = read_data()
    second_crates = re_arrange_second_crates(moves_array,crates_array)
    print("First Crates: ",first_crates, "Second Crates: ", second_crates)