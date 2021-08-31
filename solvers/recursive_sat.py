from sys import stderr
from .watchlist import update_watchlist


def solve(instance, watchlist, assignment, d, verbose):
    """
    Recursively solve SAT by assigning to variables d, d+1, ..., n-1. Assumes
    variables 0, ..., d-1 are assigned so far. A generator for all the
    satisfying assignments is returned.
    """
    if d == len(instance.variables):
        yield assignment
        return

    for a in [0, 1]:
        if verbose:
            print('Trying {} = {}'.format(instance.variables[d], a),
                  file=stderr)
        assignment[d] = a
        if update_watchlist(instance, watchlist, (d << 1) | a, assignment, verbose):
            for a1 in solve(instance, watchlist, assignment, d + 1, verbose):
                yield a1

    assignment[d] = None
