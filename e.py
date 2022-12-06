"""INPUT TEMPLATE - I copy paste this part to the top of every solution"""
import sys
 
toks = (tok for tok in sys.stdin.read().split())
"""END OF TEMPLATE"""
import math # Used to check isinf()
from collections import deque # Used for BFS
 
N = int(next(toks))
K = int(next(toks))
# To make indexing in arrays easier, I subtract all the locations by 1 so they are 0-based
x_t = int(next(toks))-1
y_t = int(next(toks))-1
knights = []
for _ in range(K):
    knights.append((int(next(toks))-1, int(next(toks))-1))
 
# min_cost[x][y] is the minimum number of hops from any of the knights to (x, y),
# or inf if it is impossible for a knight to reach that location
min_cost = [[float("inf") for _ in range(N)] for _ in range(N)]
    
# We will solve this problem using BFS
# Create a queue of all the initial locations, the knights
bfs_q = deque()
for knight_x, knight_y in knights:
    # If the min cost to this knight is already set to 0,
    # then there must have been some previous knight at this location,
    # so we can skip this knight
    if min_cost[knight_x][knight_y] == 0:
        continue
    
    bfs_q.append((knight_x, knight_y))
    # Remember to set the minimum cost of every knight to 0,
    # since you don't need to make any hops to reach that location
    min_cost[knight_x][knight_y] = 0
    
while len(bfs_q) > 0:
    cur_x, cur_y = bfs_q[0]
    bfs_q.popleft()
    # Loop through all the places we can go to with this knight:
    for new_x, new_y in [(cur_x+2, cur_y+1), (cur_x+2, cur_y-1), (cur_x-1, cur_y+2), (cur_x-1, cur_y-2), (cur_x-2, cur_y-1), (cur_x-2, cur_y+1), (cur_x+1, cur_y-2), (cur_x+1, cur_y+2)]:
        # If this location is valid (i.e. it's in the bounds of the chessboard)
        # and it hasn't been visited before (because its entry in min_cost is still inf),
        # then update the entry in min_cost and add this location to the queue
        if new_x >= 0 and new_x <= N-1 and new_y >= 0 and new_y <= N-1 and math.isinf(min_cost[new_x][new_y]):
            bfs_q.append((new_x, new_y))
            # The cost to get to (new_x, new_y) is the cost to (cur_x, cur_y),
            # plus 1 for the hop from (cur_x, cur_y) to (new_x, new_y)
            min_cost[new_x][new_y] = min_cost[cur_x][cur_y]+1
 
            # To avoid wasting time, if (new_x, new_y) is the location of the thief,
            # we can break from this loop:
            if new_x == x_t and new_y == y_t:
                break
    # If the min_cost entry of the location of the thief has been added by the above for loop,
    # then we can break from this while loop:
    if not math.isinf(min_cost[x_t][y_t]):
        break
            
# At the end, if the minimum number of hops to the location of the thief is inf,
# then it is not possible to reach the thief, so output -1:
if math.isinf(min_cost[x_t][y_t]):
    print(-1)
# Otherwise, output the cost to reach the thief:
else:
    print(min_cost[x_t][y_t])
