"""INPUT TEMPLATE - I copy paste this part to the top of every solution"""
import sys

toks = (tok for tok in sys.stdin.read().split())
"""END OF TEMPLATE"""

A = int(next(toks))
B = int(next(toks))
C = int(next(toks))
D = int(next(toks))

T = int(next(toks))
for _ in range(T):
    # N is a list of six digits:
    N = list(next(toks))
    # Use map(int, ...) to convert all the digits from strings to integers:
    E, F, G, H, I, J = map(int, N)
    # Use the % sign operator to check the conditions:
    if (100*E+10*F+I) % B == A and (100*G+10*H+J) % D == C:
        print("Yes")
    else:
        print("No")
