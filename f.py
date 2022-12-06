"""INPUT TEMPLATE - I copy paste this part to the top of every solution"""
import sys

toks = (tok for tok in sys.stdin.read().split())
"""END OF TEMPLATE"""

N = int(next(toks))
T = int(next(toks))
a = []
for _ in range(N):
    a.append(int(next(toks)))
# To make it easy to get the maximum of the array and also remove the maximum from the array,
# let's sort:
a.sort()

# First, given a probability p, we need to figure out how to compute the expected value of the game:
# Here's a way to do this using recursion, but it doesn't work:
"""
# Given an array of numbers arr and the probability p,
# compute the expected value of the number from the game in the problem statement:
def compute_expected_value(arr, p):
    # If there's only one element, then the game chooses that element:
    if len(arr) == 1:
        return arr[0]
    # Otherwise, with probability p, we choose the maximum element, which is arr[-1],
    # and with probability 1-p, we choose some element from the array without the maximum element, which is arr[:-1],
    # so take the weighted average:
    return p*arr[-1] + (1-p)*compute_expected_value(arr[:-1], p)
"""
# The reason this doesn't work is because the recursion is too much for Python to handle,
# even if you do sys.setrecursionlimit(...), you still might get a seg fault for big values of N

# Instead, we can write the same function using an iterative process:
def compute_expected_value(arr, p):
    # exp_value_of_subarray[i] is the expected value of the game with the array [arr[0], arr[1], ..., arr[i]]
    exp_value_of_subarray = []
    for i in range(N):
        # If i=0, then we are looking at the array [arr[0]], which has just one element,
        # so the expected value is just arr[0]
        if i == 0:
            exp_value_of_subarray.append(arr[0])
        else:
            # Otherwise, we are looking at the array [arr[0], ..., arr[i]]
            # Since the array is sorted, arr[i] is the maximum element,
            # so with probability p, we choose arr[i],
            # and with probability 1-p, we choose some element from [arr[0], ..., arr[i-1]],
            # and the expected value of that is just exp_value_of_subarray[i-1],
            # so take the weighted average:
            exp_value_of_subarray.append(p*arr[i] + (1-p)*exp_value_of_subarray[i-1])
    # Finally, return the expected value of [arr[0], ..., arr[N-1]] since that's the whole array:
    return exp_value_of_subarray[N-1]

# Now, we have a function that, given a probability p, gives us the expected value from the game
# Notice the function is increasing: As p goes up, the expected value goes up
# We want to find the minimum p such that compute_expected_value(arr, p) >= T,
# so we can just use binary search

lo = 0
hi = 1
# Binary search on floating-point is a bit different than binary search on integers:
# Usually we just do lo < hi when working with integers,
# but with floating-points, we don't care about an exact answer,
# so we do lo < hi-EPS instead for some value EPS.
# In the problem statement, they say an absolute value of 10^-4 is OK,
# but we'll use EPS=10^-6 just to be safe with floating-point accuracy.
EPS = 10**(-6)
while lo < hi-EPS:
    mid = (lo+hi)/2.0
    if compute_expected_value(a, mid) >= T:
        hi = mid
    else:
        lo = mid
# Finally, at the end of this while loop, we know that the answer is somewhere between lo and hi,
# since lo and hi are within 10^(-6) of each other, it's close enough to just print lo as the answer:
print(lo)
