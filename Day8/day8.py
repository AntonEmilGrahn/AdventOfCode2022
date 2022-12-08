#!/usr/bin/env python3
import numpy as np

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = list(f.read().split("\n"))
        parsed_matrix=[]
        for line in raw_array:  parsed_matrix.append(list(map(int,line)))
    return parsed_matrix

def count_visible_trees(parsed_matrix):
    no_of_trees = 0
    highest_senic_score = 0
    for r,row in enumerate(parsed_matrix):
        for c,tree in enumerate(row):
            if (r == 0 or r == len(parsed_matrix)-1) or (c == 0 or c == len(row)-1): 
                no_of_trees+=1
            else:
                trees_north = [row[c] for row in parsed_matrix[0:r]]
                trees_south = [row[c] for row in parsed_matrix[r+1:]]
                trees_east = row[c+1:]
                trees_west = row[0:c]
                if max(trees_north)<tree or max(trees_south)<tree or max(trees_east)<tree or max(trees_west)<tree: no_of_trees+=1
                north,south,east,west = 0,0,0,0
                for t in reversed(trees_north): 
                    north+= 1
                    if t>=tree: break
                for t in trees_south: 
                    south+= 1
                    if t>=tree: break
                for t in trees_east: 
                    east+= 1
                    if t>=tree: break
                for t in reversed(trees_west): 
                    west+= 1
                    if t>=tree: break 
                senic_score = north*south*east*west
                highest_senic_score = max(highest_senic_score,senic_score)
    return no_of_trees,highest_senic_score

if __name__ == "__main__":
    parsed_matrix = read_data()
    no_of_trees, highest_senic_score = count_visible_trees(parsed_matrix)
    print("Number of visible trees: ",no_of_trees, " Highest senic score: ",highest_senic_score)