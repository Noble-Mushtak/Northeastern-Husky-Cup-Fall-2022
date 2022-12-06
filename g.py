"""INPUT TEMPLATE - I copy paste this part to the top of every solution"""
import sys

toks = (tok for tok in sys.stdin.read().split())
"""END OF TEMPLATE"""

N = int(next(toks))
M = int(next(toks))
W = int(next(toks))
# For ease of indexing in arrays, I want all the vertices to be 0-based,
# so I will subtract all the vertices by 1
a = int(next(toks))-1
b = int(next(toks))-1

# adj[i] is a list of tuples (j, w, v) representing that
# there is an edge from j to i with weight w and value v
# i.e. adj[i] is a list of the incoming edges to vertex i
adj = [[] for _ in range(N)]
for _ in range(M):
    s = int(next(toks))-1
    t = int(next(toks))-1
    w = int(next(toks))
    v = int(next(toks))
    adj[t].append((s, w, v))

# For this problem, we're going to do something similar to knapsack,
# (https://en.wikipedia.org/wiki/Knapsack_problem#Dynamic_programming_in-advance_algorithm)
# but it's a little bit more tricky because we're walking on a graph,
# so we always need to keep track of the current vertex we're on in the DP state

# dp[w][i] represents the maximum value walk from a to i of weight w,
# or -inf if there is no such walk
dp = [[float("-inf") for _ in range(N)] for _ in range(W+1)]
# For weight w=0, there is a walk from a to a of weight 0, since you can just do nothing
dp[0][a] = 0

for w in range(1, W+1):
    for i in range(N):
        # As said before, dp[w][i] represents a walk from a to i of weight w
        # Since w is positive, this walk must end with some incoming edge to i
        
        # Let's say the incoming edge is from some vertex j to i and has weight w_edg
        # Then, to use this edge in a walk from a to i of weight w,
        # we will need a walk from a to j of weight w-w_edg,
        # so the subproblem we will need to solve dp[w-w_edg][j]

        # Thus, the subproblems for dp[w][i] are dp[w-w_edg][j] for all edges j to i,
        # so we need to loop through the incoming edges to vertex i:
        for j, w_edg, v_edg in adj[i]:
            # If w_edg > w, then we can't use this edge because our total walk can only have weight w,
            # so just skip this edge:
            if w_edg > w: continue

            # Otherwise, update the entry in the DP table with dp[w-w_edg][j] plus the value of this edge:
            dp[w][i] = max(dp[w][i], dp[w-w_edg][j]+v_edg)

# At the end, just print the maximum of dp[w][b] for 0 <= w <= W,
# since that's the maximum value walk from a to b of weight at most W
print(max(dp[w][b] for w in range(W+1)))
