"""INPUT TEMPLATE - I copy paste this part to the top of every solution"""
import sys

toks = (tok for tok in sys.stdin.read().split())
"""END OF TEMPLATE"""

N = int(next(toks))
K = int(next(toks))
chocolates = []
for i in range(N):
    chocolates.append((int(next(toks)), int(next(toks))))
    # For each tuple in chocolate, the first component represents s_i
    # and the second component represents p_i

# cur_pieces is the amount of chocolate pieces we have right now
# We start out with K pieces
cur_pieces = K
    
# The trick here is to do a greedy solution:
# It's always optimal to use the chocolate machines which have the lowest s_i first
# Therefore, we just sort the chocolates in order and loop through and use as many as possible:
chocolates.sort()
for s_i, p_i in chocolates:
    # We need cur_pieces >= s_i to use this machine:
    if cur_pieces >= s_i:
        # Add cur_pieces by p_i-s_i, because the machine takes s_i pieces but then produces p_i pieces
        cur_pieces += p_i-s_i
        
print(cur_pieces)
