import sys

with open(sys.argv[1], 'r') as file:
    input_data = file.read()
    lines = input_data.strip().split('\n')

n_list = []
gr = {}
gr_k = 1
n_line = 0

while n_line < len(lines) - 1:
    graph_order = int(lines[n_line])
    i = n_line + 1

    while i < n_line + graph_order + 1:
        n_list.append([int(n) for n in lines[i].split()])
        i += 1

    gr[gr_k] = n_list
    n_list = []
    gr_k += 1
    n_line += graph_order + 1


def undirected_girth(gr):
    n = len(gr)
    smallest = float('inf')

    r = 0
    while r < n - 2:
        level = [-1] * n
        level[r] = 0
        to_grow = [r]

        while to_grow:
            grow = to_grow.pop(0)
            if level[grow] * 2 + 1 > smallest:
                break

            neighbors = gr[grow]
            for u in neighbors:
                if u < r:
                    continue

                if level[u] < 0:
                    level[u] = level[grow] + 1
                    to_grow.append(u)
                elif level[u] == level[grow]:
                    smallest = min(smallest, level[u] * 2 + 1)
                    break
                elif level[u] == level[grow] + 1:
                    smallest = min(smallest, level[u] * 2)
                    break

        r += 1

    if smallest == float('inf'):
        return 'infinity'

    return smallest


# Example usage:
# Representing a graph as an adjacency list
for key in gr.keys():
    print("Graph {} has girth {}.".format(key, undirected_girth(gr[key])))