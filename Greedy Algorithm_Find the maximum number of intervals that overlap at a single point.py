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
            sorted_test = sorted(test, key=lambda x: x[0])
            nested_lists[test_index] = sorted_test
            test_index += 1
    except StopIteration:
        break

def max_intervals_overlap(intervals):
    # Combine start and end points of intervals with type and index
    points = []
    for i, (start, end) in enumerate(intervals):
        points.append((start, 'start', i))
        points.append((end, 'end', i))

    # Sort points based on their positions
    points.sort(key=lambda x: (x[0], x[1] != 'start'))

    # Traverse through the points and keep track of maximum overlap
    max_overlap = 0
    current_overlap = 0
    active_intervals = set()
    active_a = set()
    active_b = set()  # To keep track of currently active intervals
    for point, event, index in points:
        if event == 'start' or point == active_b:
            current_overlap += 1
            active_intervals.add(index)
            active_b.add(intervals[index][0])
            active_b.add(intervals[index][1])
            max_overlap = max(max_overlap, current_overlap)
        elif event == 'end' and point not in active_a:
            current_overlap -= 1
            if index in active_intervals:
                active_intervals.remove(index)

    return max_overlap

for k, value in test_fr.items():
   for intervals in value:
       print(max_intervals_overlap(intervals))
