graph = {
    'a': set(['b', 'c', 'd']),
    'b': set(),
    'c': set(['e']),
    'd': set(['e']),
    'e': set([]),
}
​
all_paths = []
def print_graph(current_vertex, path):
    print(current_vertex)
    # Recurse on the children
    new_path = path + [current_vertex]
    # I have reached the end of my path because the neighbor is empty
    if len(graph[current_vertex]) == 0:
        all_paths.append(new_path)
​
    for neighbor in graph[current_vertex]:
        print_graph(neighbor, new_path.copy())
​
​
print_graph('a', [])
print(all_paths)