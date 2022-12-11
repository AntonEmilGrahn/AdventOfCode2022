#!/usr/bin/env python3
def read_data():
    with open('data.txt', 'r') as f:
        raw_array = list(f.read().split("\n"))
        parsed_array=[]
        for line in raw_array: parsed_array.append(line.split(" "))
    return parsed_array

class Dir:
  def __init__(self,name,parent,children,data):
    self.name = name
    self.parent = parent
    self.children = children
    self.data = data

def backwards_propogate_tree(current_node,data):
    current_node.data+=int(data)
    if current_node.parent is not None: backwards_propogate_tree(current_node.parent,data)
    
def build_tree(parsed_array):
    root = Dir('/',None,[],0)
    current_node = root
    for c in parsed_array:
        if c[0] =='$':
            if c[1] == 'cd':
                if c[2] == '..': current_node = current_node.parent
                if c[2] == '/': current_node = root
                else: 
                    for child in current_node.children: 
                        if child.name == c[2]: current_node = child
        elif c[0] =='dir':
            new_node = Dir(c[1],current_node,[],0)
            current_node.children.append(new_node)
        elif c[0].isnumeric():
            backwards_propogate_tree(current_node,c[0])
    return root

def calculate_data(node,data_threshold,score_node):
    if node.data<=data_threshold: 
        score_node.data+=int(node.data)
    for child in node.children: calculate_data(child,data_threshold,score_node)

def find_delete_file(node,data_to_be_cleared,delete_node):
    if node.data>=data_to_be_cleared: 
        delete_node.data = min(node.data,delete_node.data)
    for child in node.children: find_delete_file(child,data_to_be_cleared,delete_node)

if __name__ == "__main__":
    parsed_array = read_data()
    root = build_tree(parsed_array)
    score_node = Dir('',None,[],0)
    data_threshold = 100000
    calculate_data(root,data_threshold,score_node)
    data_to_be_cleared = abs(70000000-30000000-int(root.data))
    delete_node = Dir('',None,[],70000000)
    find_delete_file(root,data_to_be_cleared,delete_node)
    print("Data Size: ",score_node.data, " Size To Delete: ", delete_node.data)