import sys

with open(sys.argv[1], 'r') as file:
    input_data = file.read()
    lines = input_data.strip().split('\n')

test = {}
current_key = None
index = 0
total_lines = len(lines)

while index < total_lines:
    line = lines[index]
    parts = line.split()
    if len(parts) == 1:
        current_key = int(parts[0])
        if current_key not in test:
            test[current_key] = []
    else:
        test[current_key].append([int(x) for x in parts])
    index += 1

index = 0
total_keys = len(test)

while index < total_keys:
    key = list(test.keys())[index]
    lists = test[key]
    differences = []
    list_index = 0
    total_lists = len(lists)
    while list_index < total_lists:
        sublist = lists[list_index]
        sum_a = sum(sublist[i] for i in range(0, len(sublist), 2))
        sum_b = sum(sublist[i] for i in range(1, len(sublist), 2))
        differences.append(sum_b - sum_a)
        list_index += 1
    for diff in differences:
        print(diff)
    index += 1
