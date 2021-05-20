# A matrix must be a square 
# adding is 0(v)

# class Graph:
#   def __init__(self)

graph_map = {'a': 0}

graph = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
]

# get the second vertex and its edges 
second_vertex = graph[1]

#find out if, third and last vertex are connected
print(graph[2][4] == 1)




#make a new connection from B to E
graph[1][4] = 1

graph = {
    'a': set(['b', 'c', 'd']),
    'b': set(),
    'c': set(['e']),
    'd': set(['e']),
    'e': set(),
}

# Find out if, C connects to E 
print('e' in graph['c'])

# Find out if A snd E are connected?
print('e' in graph['a'])

all_paths = []
def print_graph(current_vertex, path):
    print(current_vertex)
    # recurse the children 
    new_path = path + [current_vertex]
    # I have reached the end of my path because...
    if len(graph[current_vertex]) == 0:
        all_paths.append(new_path)

    for neighbor in graph[current_vertex]:
        print_graph(neighbor, new_path.copy())

print_graph('a', [])
print(all_paths)


def print_tree_pre_order(root):
    print(root.value)
    # if you can go left, recurse left 
    if root.left:
        print_tree_pre_order(root.left)

    if root.right:
        print_tree_pre_order(root.right)