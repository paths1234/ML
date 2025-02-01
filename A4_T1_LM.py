import sys

with open(sys.argv[1], 'r') as file:
    input = file.read()
    lines = input.strip().split('\n')

gr = {}
i_gr = 1
n_line = 0

while n_line < len(lines) - 1:
    order_gr = int(lines[n_line])
    n_list = []

    for i in range(n_line + 1, n_line + order_gr + 1):
        n_list.append(lines[i].split())

    gr[i_gr] = n_list
    i_gr += 1
    n_line += order_gr + 1

for j in gr.keys():
    count = sum(len(inner_list) for inner_list in gr[j])
    print('Graph {} has size {}.'.format(j, int(count) // 2))