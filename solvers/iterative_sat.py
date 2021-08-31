from sys import stderr
from .watchlist import update_watchlist


def solve(instance, watchlist, assignment, d, verbose):
    n = len(instance.variables)
    state = [0] * n
    while True:
        if d == n:
            yield assignment
            d -= 1
            continue
        # Let's try assigning a value to v. Here would be the place to insert
        # heuristics of which value to try first.
        tried_something = False
        for a in [0, 1]:
            if (state[d] >> a) & 1 == 0:
                if verbose:
                    print('Trying {} = {}'.format(instance.variables[d], a),
                          file=stderr)
                tried_something = True
                # Set the bit indicating a has been tried for d
                state[d] |= 1 << a
                assignment[d] = a
                if not update_watchlist(instance, watchlist, d << 1 | a, assignment, verbose):
                    assignment[d] = None
                else:
                    d += 1
                    break

        if not tried_something:
            if d == 0:
                return
            else:
                state[d] = 0
                assignment[d] = None
                d -= 1
