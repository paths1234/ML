import sys

with open(sys.argv[1], 'r') as file:
    input = file.read()
    lines = input.strip().split('\n')

n_list = []
gr = {}
gr_index = 1
n_line = 0

while n_line < len(line) - 1:
    gr_order = int(line[n_line])

    for i in range(n_line + 1, n_line + gr_order + 1):
        n_list.append([int(n) for n in line[i].split()])

    gr[gr_index] = n_list
    num_list = []
    gr_index += 1
    n_line += gr_order + 1

def bfs(start_node, gr, visited):
    queue = [start_node]
    visited[start_node] = True

    while queue:
        curr_node = queue.pop(0)

        for neighbor in gr[curr_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def diameter(start_node, gr):
    queue = [(start_node, 0)]
    visited = [False] * len(gr)
    visited[start_node] = True
    max_distance = 0

    while queue:
        current_node, distance = queue.pop(0)
        max_distance = max(max_distance, distance)

        for neighbor in gr[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))

    return max_distance

def disconnected(gr):
    visited = [False] * len(gr)
    for start_node in range(len(gr)):
        if not visited[start_node]:
            bfs(start_node, gr, visited)
            if not all(visited):
                return True
    return False

for key in gr.keys():
    if disconnected(gr[key]):
        print('Graph {} is disconnected.'.format(key))
    else:
        max_distance = 0
        for start_node in range(len(gr[key])):
            max_distance = max(max_distance, diameter(start_node, gr[key]))
        print("Graph {} has diameter {}.".format(key, max_distance))
