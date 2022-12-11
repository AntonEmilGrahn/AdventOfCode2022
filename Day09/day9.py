#!/usr/bin/env python3

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        parsed_array = []
        for element in raw_array:
            parsed_array.append(element.split(" "))
    return parsed_array

def record_step(no_of_positions,tail_position,visited_positions):
    if tail_position not in visited_positions:
        visited_positions.append(tail_position)
        no_of_positions+=1
    return no_of_positions,visited_positions

def find_positions(parsed_array):
    no_of_positions = 1
    head_position = [0,0]
    tail_position = [0,0]
    visited_positions = [tail_position]
    position_log = [tail_position]
    for head_move in parsed_array:
        dir = head_move[0]
        for step in range(int(head_move[1])):
            if dir == 'U': 
                head_position = [head_position[0]+1,head_position[1]]
                if abs(head_position[0]-tail_position[0])>1 or abs(head_position[1]-tail_position[1])>1:
                    tail_position = [head_position[0]-1,head_position[1]]
                    position_log.append(tail_position)
                    no_of_positions,visited_positions = record_step(no_of_positions,tail_position,visited_positions)
            if dir == 'D': 
                head_position = [head_position[0]-1,head_position[1]]
                if abs(head_position[0]-tail_position[0])>1 or abs(head_position[1]-tail_position[1])>1:
                    tail_position = [head_position[0]+1,head_position[1]]
                    position_log.append(tail_position)
                    no_of_positions,visited_positions = record_step(no_of_positions,tail_position,visited_positions)
            if dir == 'L': 
                head_position = [head_position[0],head_position[1]-1]
                if abs(head_position[0]-tail_position[0])>1 or abs(head_position[1]-tail_position[1])>1:
                    tail_position = [head_position[0],head_position[1]+1]
                    position_log.append(tail_position)
                    no_of_positions,visited_positions = record_step(no_of_positions,tail_position,visited_positions)
            if dir == 'R': 
                head_position = [head_position[0],head_position[1]+1]
                if abs(head_position[0]-tail_position[0])>1 or abs(head_position[1]-tail_position[1])>1:
                    tail_position = [head_position[0],head_position[1]-1]
                    position_log.append(tail_position)
                    no_of_positions,visited_positions = record_step(no_of_positions,tail_position,visited_positions)
    return no_of_positions, position_log

def find_positions_tail(position_log):
    no_of_positions = 1
    tail_position = [0,0]
    head_coords = [0,0]
    visited_positions = [tail_position]
    new_position_log = [tail_position]
    for head_coords in position_log:
        if abs(head_coords[0]-tail_position[0])>1 or abs(head_coords[1]-tail_position[1])>1:
            vertical = head_coords[0]-tail_position[0]
            horizontal = head_coords[1]-tail_position[1]
            if (abs(vertical)==2 and abs(horizontal)==0) or (abs(horizontal)==2 and vertical==0):
                tail_position = [tail_position[0]+int(vertical/2),tail_position[1]+int(horizontal/2)]
            elif abs(vertical)==2 and abs(horizontal)==1:
                tail_position = [tail_position[0]+int(vertical/2),tail_position[1]+horizontal]
            elif abs(horizontal)==2 and abs(vertical)==1:
                tail_position = [tail_position[0]+vertical,tail_position[1]+int(horizontal/2)]
            elif abs(horizontal)==2 and abs(vertical)==2:
                tail_position = [tail_position[0]+(vertical/2),tail_position[1]+int(horizontal/2)]
            new_position_log.append(tail_position)
            no_of_positions,visited_positions = record_step(no_of_positions,tail_position,visited_positions)
    return no_of_positions,new_position_log

def long_tail(parsed_array):
    tail_extention = 8
    no_of_positions,position_log = find_positions(parsed_array)
    for i in range(tail_extention):
        no_of_positions,position_log = find_positions_tail(position_log)
    return no_of_positions 

if __name__ == "__main__":
    parsed_array = read_data()
    no_of_positions,position_log = find_positions(parsed_array)
    no_of_long_positions = long_tail(parsed_array)
    print("First Score: ",no_of_positions, "Second Score: ",no_of_long_positions)