import io
from sys import stderr
from typing import List

f = open("test.txt", "r")
lines = f.readlines()
_list = []
for k in lines[1:]:
    line1 = k.strip()
    line = line1.split(" ")
    a = [int(j) for j in line[:-1]]
    _list.append(a)

str1 = ' '
str2 = str1.join(str(_list))
stdin = io.StringIO('''2
3 3
X1 v X2
~X1
~X2 v X3
3 5
X1 v X2 v X3
X1 v ~X2
X2 v ~X3
X3 v ~X1
~X1 v ~X2 v ~X3
'''
                    )


def get_reverse(literal1: str) -> str:
    if literal1[0] == '~':
        return literal1[1:]
    return '~' + literal1


def update_list():
    pass


def recursive(clasue_Set, Pasrtial_assignment):
    verbose = True
    d = 40
    if update_watchlist(clasue_Set, watchlist, (d << 1), Pasrtial_assignment, verbose):
        for a1 in recursive(clasue_Set, Pasrtial_assignment):
            yield a1
        return

    for a in [0, 1]:
        if verbose:
            print('Trying {} = {}'.format(clasue_Set.variables[d], a),
                  file=stderr)
        Pasrtial_assignment[d] = a
    Pasrtial_assignment[d] = None


def parse_clause() -> List[str]:
    return stdin.readline().strip().split(' v ')


n_cases = int(stdin.readline())
print(_list[4:9])
for _ in range(n_cases):
    n_vars, n_clauses = (int(s) for s in stdin.readline().split())
    my_sets = [{c} for c in parse_clause()]
    for _ in range(n_clauses - 1):
        temp_sets = []
        current_clause = parse_clause()

        for s in my_sets:
            for literal in current_clause:
                if get_reverse(literal) not in s:
                    new_set = s.copy()
                    new_set.add(literal)
                    temp_sets.append(new_set)

        my_sets = temp_sets

    if my_sets:
        print('satisfiable')
    else:
        print('unsatisfiable')
