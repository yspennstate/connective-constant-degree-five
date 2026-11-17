"""Exact check of the atom shapes in the proof for degree five (Section 5 of the paper).

For each (a, e) with a >= 2, e >= 1 and a*e <= 4, list every loopless (5-e)-regular multigraph on a labelled vertex
set {0, ..., a-1} that satisfies the strict cut condition e|S| + |E(S, A-S)| > a e for every proper nonempty S.
For each, compute the path sums P_uw(1/2) by enumerating self-avoiding paths, the child weights at every entry
vertex, the function W, its lower convex envelope psi at c = (a e - 2)/2, and print psi(c). Arithmetic is exact
(fractions) up to the final logarithm; the weights and W are printed as exact fractions.
Python 3 standard library only; runs in a second.
"""
import itertools
import math
from fractions import Fraction as F

t = F(1, 2)


def multigraphs(a, deg):
    pairs = list(itertools.combinations(range(a), 2))
    for ms in itertools.product(range(deg + 1), repeat=len(pairs)):
        m = dict(zip(pairs, ms))
        if all(sum(m[p] for p in pairs if v in p) == deg for v in range(a)):
            yield m


def mult(m, u, v):
    return m[(min(u, v), max(u, v))]


def cut_ok(m, a, e):
    for k in range(1, a):
        for S in itertools.combinations(range(a), k):
            out = sum(mult(m, u, v) for u in S for v in range(a) if v not in S)
            if e * len(S) + out <= a * e:
                return False
    return True


def path_sum(m, a, u, w):
    if u == w:
        return F(1)
    total = F(0)
    others = [x for x in range(a) if x not in (u, w)]
    for k in range(len(others) + 1):
        for mid in itertools.permutations(others, k):
            seq = (u,) + mid + (w,)
            n = 1
            for x, y in zip(seq, seq[1:]):
                n *= mult(m, x, y)
            total += n * t ** (len(seq) - 1)
    return total


def psi(W, c):
    """Lower convex envelope of log W on {0, ..., len(W)-1}, evaluated at c: the least chord value over i <= c <= j."""
    L = [math.log(x) for x in W]
    best = None
    for i in range(len(W)):
        for j in range(i, len(W)):
            if i <= c <= j and (i < j or i == c):
                v = L[i] if i == j else ((j - c) * L[i] + (c - i) * L[j]) / (j - i)
                best = v if best is None else min(best, v)
    return best


for a, e in [(2, 1), (2, 2), (3, 1), (4, 1)]:
    deg = 5 - e
    c = F(a * e - 2, 2)
    shapes = [m for m in multigraphs(a, deg) if cut_ok(m, a, e)]
    worst = None
    for m in shapes:
        for u in range(a):
            weights = [t] * (e - 1)
            for w in range(a):
                if w != u:
                    weights += [t * path_sum(m, a, u, w)] * e
            weights.sort()
            W = [sum(weights[: b + 1]) for b in range(len(weights))]
            v = psi(W, float(c))
            if worst is None or v < worst[0]:
                worst = (v, u, {p: k for p, k in m.items() if k}, W)
    print("a=%d e=%d: %d labelled atom shapes; least psi(c) = %.12f at entry %d, shape %s, W = %s"
          % (a, e, len(shapes), worst[0], worst[1], worst[2], [str(x) for x in worst[3]]))
