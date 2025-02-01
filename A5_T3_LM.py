import sys

with open(sys.argv[1], 'r') as file:
    input_data = file.read()
    lines = input_data.strip().split('\n')

input = {}
input_key = None
index = 0
total_lines = len(lines)

while index < total_lines:
    line = lines[index]
    parts = line.split()
    if len(parts) == 1:
        input_key = int(parts[0])
        if input_key not in input:
            input[input_key] = []
    else:
        input[input_key].append([int(x) for x in parts])
    index += 1

test_fr = {}
input_iterator = iter(input.items())
while True:
    try:
        k, nested_list = next(input_iterator)
        test_fr[k] = [[(x, y) for x, y in zip(v[::2], v[1::2])] for v in nested_list]
    except StopIteration:
        break

test_iterator = iter(test_fr.items())
while True:
    try:
        k, nested_lists = next(test_iterator)
        test_index = 0
        while test_index < len(nested_lists):
            test = nested_lists[test_index]
            sorted_test = sorted(test, key=lambda x: x[1])
            nested_lists[test_index] = sorted_test
            test_index += 1
    except StopIteration:
        break

a_lists = []
b_lists = []

test_iterator = iter(test_fr.items())
while True:
    try:
        k, nested_lists = next(test_iterator)
        test_index = 0
        while test_index < len(nested_lists):
            test = nested_lists[test_index]
            sorted_test = sorted(test, key=lambda x: x[1])
            nested_lists[test_index] = sorted_test

            a_lists.append([x[0] for x in sorted_test])
            b_lists.append([x[1] for x in sorted_test])

            test_index += 1
    except StopIteration:
        break

i = 0
while i < len(a_lists):
    a = 1
    b = 0
    up_bound = [b_lists[i][b]]
    while a < len(a_lists[i]) and b < (len(b_lists[i]) - 1):
        if a_lists[i][a] <= b_lists[i][b]: #overlapping
            a += 1
        else:
            up_bound.append(b_lists[i][a])
            b = a
            a += 1
    print(len(up_bound))
    i += 1