#!/usr/bin/env python3

def read_data():
    with open('minidata.txt', 'r') as f:
        raw_array = list(f.read().split("\n"))
        parsed_array=[]
        for line in raw_array: parsed_array.append(line.split(" "))
        print(parsed_array)
    return parsed_array

class Dir:
  def __init__(self,name,parent,children,data):
    self.name = name
    self.parent = parent
    self.children = children
    self.data = data

def build_tree(parsed_array):
    root = Dir('/',None,[],0)
    current_node = root
    found_nodes = ['/']
    state = None
    for command in parsed_array:
        if command[0] =='$':
            if command[1] == 'cd':
                print("cd: ",command[2])
            elif command[1] == 'dir':
                print("dir: ",command[2])
            elif command[1] == 'ls':
                print("ls",)
        elif command[0] =='dir':
            print("dir: ",command[1])
            if command[1] not in found_nodes:
                new_node = Dir(command[1],current_node,[],0)
                current_node.children.append(new_node)
                current_node = new_node
            else: pass #if we already have found node
        elif command[0].isnumeric():
            print("data: ",command[0])
            current_node.data+=int(command[0])
        print(current_node.data)

def calculate_free_space(root):
    score = 0 
    return score
    
if __name__ == "__main__":
    parsed_array = read_data()
    first_score = build_tree(parsed_array)
    second_score = build_tree(parsed_array)
    print("First Score: ",first_score, "Second Score: ", second_score)