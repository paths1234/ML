import sys

with open(sys.argv[1], 'r') as file:
    input = file.read()
    line = input.strip().split('\n')

def adjacency_list_to_matrix(adj_list):
    n_v = len(adj_list)
    adj_matrix = [[0] * n_v for _ in range(n_v)]
    for vertex, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            adj_matrix[vertex][neighbor] = 1
    return adj_matrix

gr = {}
gr_index = 1
n_line = 0

while n_line < len(line) - 1:
    gr_order = int(line[n_line])
    adj_list = []

    for i in range(n_line + 1, n_line + gr_order + 1):
        adj_list.append([int(n) for n in line[i].split()])

    adj_matrix = adjacency_list_to_matrix(adj_list)
    gr[gr_index] = adj_matrix
    gr_index += 1
    n_line += gr_order + 1

for key, matrix in gr.items():
    num_vertices = len(matrix)
    print(num_vertices)

    for row in matrix:
        print(*row)

print('0')  # Signal the end of graphs
