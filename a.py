"""INPUT TEMPLATE - I copy paste this part to the top of every solution"""
import sys

toks = (tok for tok in sys.stdin.read().split())
"""END OF TEMPLATE"""

N = int(next(toks))
a = []
for _ in range(N):
    a.append(int(next(toks)))

# If N=1, then just output the single array element and exit:
if N == 1:
    print(a[0])
    sys.exit(0) # Exits the program with no error
    
# First, implement Dr. Ickelboom's sum function in Python:
def ickelboom_sum(x, y):
    return 5*(x//5)+5*(y//5)+min(4, (x-5*(x//5))*(y-5*(y//5)))

# Then apply that ickelboom_sum function across the array:
ans = ickelboom_sum(a[0], a[1])
for i in range(2, N):
    ans = ickelboom_sum(ans, a[i])
print(ans)
