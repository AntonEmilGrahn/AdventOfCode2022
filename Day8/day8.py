#!/usr/bin/env python3
import numpy as np

def read_data():
    with open('data.txt', 'r') as f:
        raw_array = list(f.read().split("\n"))
        parsed_array=np.array([])
        for line in raw_array: np.vstack((parsed_array,line.split()))
        print(parsed_array)
    return parsed_array

if __name__ == "__main__":
    parsed_array = read_data()
    print("Data Size: ", " Size To Delete: " )