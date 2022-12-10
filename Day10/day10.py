#!/usr/bin/env python3

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = f.read().split("\n") 
        parsed_array = []
        for element in raw_array:
            parsed_array.append(element.split(" "))
    return parsed_array

def draw_pixel(position, sprite_center, screen_output,line_breakers,line_correction):
    sprite = [sprite_center-1,sprite_center,sprite_center+1]
    if position in line_breakers: 
        screen_output+='\n'
        line_correction = position-1
    if position-line_correction in sprite: screen_output+='#'
    else: screen_output+='.'
    return screen_output,line_correction

def find_signal_strength(parsed_array):
    signal_strengths = []
    check_cycles = [20,60,100,140,180,220]
    signal_sum, cycles, total_value  = 0,0,1
    screen_output = ''
    line_breakers = [39,79,119,159,199,239]
    line_correction = -2
    for command in parsed_array:
        if command[0] == 'noop': 
            screen_output,line_correction=draw_pixel(cycles-1,total_value+1,screen_output,line_breakers,line_correction)
            cycles+=1
            if cycles in check_cycles: signal_strengths.append(total_value*cycles,)
        if command[0] == 'addx':
            screen_output,line_correction=draw_pixel(cycles-1,total_value+1,screen_output,line_breakers,line_correction)
            cycles+=1
            if cycles in check_cycles: signal_strengths.append(total_value*cycles)
            screen_output,line_correction=draw_pixel(cycles-1,total_value+1,screen_output,line_breakers,line_correction)
            cycles+=1
            if cycles in check_cycles: signal_strengths.append(total_value*cycles)
            total_value+=int(command[1])
    signal_sum = sum(signal_strengths)
    return signal_sum, screen_output

if __name__ == "__main__":
    parsed_array = read_data()
    signal_sum,screen_output = find_signal_strength(parsed_array)
    print("First Score: ",signal_sum)
    print(screen_output)