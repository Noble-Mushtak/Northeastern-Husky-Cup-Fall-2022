"""INPUT TEMPLATE - I copy paste this part to the top of every solution"""
import sys

toks = (tok for tok in sys.stdin.read().split())
"""END OF TEMPLATE"""

T = int(next(toks))
for _ in range(T):
    N = int(next(toks))
    K = int(next(toks))

    # centers[i] represents the location of the center of the ith plank
    centers = []
    # sum_centers represents the sum of the length of all the planks we have seen so far
    sum_planks = 0
    for i in range(N):
        cur_length = int(next(toks))
        # The center of this plank is located at the sum of all the previous planks + half the length of this plank:
        centers.append(sum_planks + cur_length//2)
        # Update sum_planks:
        sum_planks += cur_length

    # If there are <=K+2 planks, then Juli should just stand on the first and last plank to maximize distance:
    if N <= K+2:
        print(centers[N-1] - centers[0])
    else:
        # Otherwise, Juli should stand on plank i and plank i+K+1 for some index i
        # So let's just loop through all possible indexes i and then take the one which gives us the max distance
        mx_dist = 0
        for i in range(N-K-1):
            mx_dist = max(mx_dist, centers[i+K+1] - centers[i])
        print(mx_dist)
