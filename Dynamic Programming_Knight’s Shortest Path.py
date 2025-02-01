import sys

input = sys.stdin.read()
lines = input.split('\n')

# Extract board sizes
n = []
m = []
index = 0

while index < len(lines):
    if lines[index] != '':
        first, second = map(int, lines[index].split())
        n.append(first)
        m.append(second)
    index += 1

# Function to check if a position is within bounds
def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# Function to find the shortest path and count distinct paths using BFS
def shortest_path(board_n, board_m):
    # Possible moves for a knight
    knight_moves = [(1, 2), (-1, 2), (2, 1), (-2, 1), (1, -2), (-1, -2), (2, -1), (-2, -1)]

    # Initialize the chessboard with infinity distances
    distances = [[float('inf')] * board_m for _ in range(board_n)]
    path_counts = [[0] * board_m for _ in range(board_n)]  # Store the number of distinct paths

    # Starting point (top-left corner)
    start_x, start_y = 0, 0
    distances[start_x][start_y] = 0
    path_counts[start_x][start_y] = 1

    # Queue for BFS
    queue = [(start_x, start_y)]
    queue_start = 0

    while queue_start < len(queue):
        x, y = queue[queue_start]
        queue_start += 1
        current_distance = distances[x][y]

        # Check all possible moves for the knight
        move_index = 0
        while move_index < len(knight_moves):
            dx, dy = knight_moves[move_index]
            new_x, new_y = x + dx, y + dy
            move_index += 1

            if is_valid(new_x, new_y, board_n, board_m):
                if current_distance + 1 < distances[new_x][new_y]:
                    distances[new_x][new_y] = current_distance + 1
                    path_counts[new_x][new_y] = path_counts[x][y]
                    queue.append((new_x, new_y))
                elif current_distance + 1 == distances[new_x][new_y]:
                    path_counts[new_x][new_y] += path_counts[x][y]

    # Return the distance to the bottom-right corner and the number of distinct paths
    return distances[board_n - 1][board_m - 1], path_counts[board_n - 1][board_m - 1]

# Process each test case
case_index = 0
while case_index < len(m):
    shortest, distinct_paths = shortest_path(n[case_index], m[case_index])
    if shortest == float('inf') and distinct_paths == 0:
        break
    print(shortest, distinct_paths)
    case_index += 1
