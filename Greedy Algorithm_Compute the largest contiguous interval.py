import sys

input = sys.stdin.read()
lines = input.strip().split('\n')

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


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged

def cont_intervals(intervals):
    merged_intervals = merge_intervals(intervals)
    max_length = 0
    for interval in merged_intervals:
        length = interval[1] - interval[0]
        if length > max_length:
            max_length = length

    return max_length

for k, value in test_fr.items():
   for intervals in value:
       print(cont_intervals(intervals))
