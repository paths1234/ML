import sys

def longest_paper_chain(n, triangles):
    triangles.sort(key=lambda x: x[3])

    # DP array to store the chain length and used sides for each triangle
    dp = [[1 for _ in range(3)] for _ in range(n)]  # Each triangle is a chain of length 1 by itself
    max_chain_length = 0

    # Process each triangle
    for i in range(n):
        for j in range(3):
            for k in range(i):
                if triangles[i][3] <= triangles[k][3]:
                    break
                for l in range(3):
                    if triangles[i][j] == triangles[k][l]:
                        dp[i][j] = max(dp[i][j], dp[k][(l+1)%3] + 1)
                        dp[i][j] = max(dp[i][j], dp[k][(l+2)%3] + 1)
            max_chain_length = max(max_chain_length, dp[i][j])
    
    return max_chain_length

# Input reading
input_data = sys.stdin.read()
lines = input_data.strip().split('\n')
    
datasets = []
index = 0
while index < len(lines):
    if lines[index].strip() == '':
        index += 1
        continue
        
    n = int(lines[index])
    index += 1
    triangles = []
        
    for _ in range(n):
        l1, l2, l3, g = lines[index].split()
        l1, l2, l3 = int(l1), int(l2), int(l3)
        g = float(g)
        triangles.append((l1, l2, l3, g))
        index += 1
  
    datasets.append((n, triangles))

# Calculate the longest chain
result = longest_paper_chain(n, triangles)
print(result)
