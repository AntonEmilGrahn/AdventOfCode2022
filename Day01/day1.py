#!/usr/bin/env python3
import numpy as np

def main():
    with open('data.txt', 'r') as f:
        txt = f.read()
        raw_array = txt.split("\n\n")
        sum_array = []
        for element in raw_array:
            array = element.split("\n")
            array = [eval(i) for i in array]
            sum_array.append(np.sum(array))
        max_value = max(sum_array)
        sorted_array = np.sort(sum_array)
        three_largest = sum(sorted_array[-3:])
    return max_value,three_largest

if __name__ == "__main__":
    max_value,three_largest = main()
    print("Biggest is: ",max_value, "Three largest combined are: ", three_largest)