input_string = '''7
1 3 0 2 3 4
0 3 1 2 1 3 4 4
0 2 3 4 5 6 3 6 2 4
1 1 1 2 1 3 1 4 1 5
0 1 1 2 2 3 4 4 6 6
1 2 4 4 4 5 6 6 5 6 
0 1 3 4 5 6 5 7 6 7
3
0 2 3 4 5 6 3 6 2 4
1 4 2 2 3 3 5 6 8 9
1 1 1 1 1 1 1 1 1 1'''

lines = input_string.strip().split('\n')

input_data = {}
current_key = None

line_index = 0
while line_index < len(lines):
    line = lines[line_index]
    parts = line.split()
    if len(parts) == 1:
        current_key = int(parts[0])
        if current_key not in input_data:
            input_data[current_key] = []
    else:
        intervals = [(int(parts[i]), int(parts[i+1])) for i in range(0, len(parts), 2)]
        input_data[current_key].append(intervals)
    line_index += 1

def min_gap(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    a_list = [interval[0] for interval in sorted_intervals]
    b_list = [interval[1] for interval in sorted_intervals]

    smallest_diff = float('inf')
    smallest_a = None
    smallest_b = None

    b_index = 0
    while b_index < len(b_list):
        b = b_list[b_index]
        a_index = 0
        while a_index < len(a_list):
            a = a_list[a_index]
            if b < a:
                diff = a - b
                if diff == 1:
                    return 1
                if diff < smallest_diff:
                    smallest_diff = diff
                    smallest_a = a
                    smallest_b = b
            a_index += 1
        b_index += 1

    if smallest_diff == 0 or smallest_diff == float('inf'):
        return max(b_list) - min(a_list)
    else:
        return smallest_diff

key_index = 0
keys = list(input_data.keys())
while key_index < len(keys):
    key = keys[key_index]
    test_fr = input_data[key]
    test_index = 0
    while test_index < len(test_fr):
        intervals = test_fr[test_index]
        result = min_gap(intervals)
        print(result)
        test_index += 1
    key_index += 1