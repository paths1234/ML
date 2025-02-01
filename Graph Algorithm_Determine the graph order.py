import sys

# reading input
with open(sys.argv[1], 'r') as file:
    input = file.read()
    line = input.strip().split('\n')

n_list = []
gr = {}
gr_index = 1
n_line = 0

while n_line < len(line) - 1:
  gr_order = int(line[n_line])

  for i in range(n_line + 1, n_line + gr_order + 1):
    n_list.append([int(n) for n in line[i].split()])

  gr[gr_index] = n_list
  n_list = []
  gr_index += 1
  n_line += gr_order + 1

def largest_component(gr):
    n_node = len(gr)
    visit = [False] * n_node
    component_order = []

    for node in range(n_node):
        if not visit[node]:
            order = dfs(node, gr, visit)
            component_order.append(order)

    return max(component_order)

def dfs(node, gr, visited):
    s = [node]
    component_order = 0

    while s:
        a = s.pop()
        if not visited[a]:
            visited[a] = True
            component_order += 1
            for i in gr[a]:
                s.append(i)

    return component_order

for i in gr.keys():
  max_order = largest_component(gr[i])
  print("Graph {} has a component of order {}.".format(i, max_order))
