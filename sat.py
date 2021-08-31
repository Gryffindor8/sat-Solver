from sys import stderr
from satinstance import SATInstance
from solvers.watchlist import setup_watchlist
from solvers import iterative_sat


def generate_assignmnets(instance, solver, verbose=False):
    n = len(instance.variables)
    watchlist = setup_watchlist(instance)
    if not watchlist:
        return ()
    assignment = [None] * n
    return solver.solve(instance, watchlist, assignment, 0, verbose)


def run_solver(brief, verbose, output_all):
    instance = SATInstance.from_file("test.txt")
    starting_with = "-"
    assignments = generate_assignmnets(instance, iterative_sat, verbose)
    count = 0
    for assignment in assignments:
        count += 1
        if verbose:
            print('Found satisfying assignment #{}:'.format(count),
                  file=stderr)
        assignment_str = instance.assignment_to_string(
            assignment,
            brief=brief,
            starting_with=starting_with
        )
        output_filee = open("out.txt", "w")
        output_filee.write(assignment_str + '\n')
        if not output_all:
            break

    if verbose and count == 0:
        print('No satisfying assignment exists.', file=stderr)


def main():
    run_solver("store_const", True, "")
    # args = parse_args()
    # with args.input:
    #     with args.output:
    #         run_solver(args.output, args.brief,
    #                    args.verbose, args.all, args.starting_with)


# def parse_args():
#     parser = ArgumentParser(description=__doc__)
#     parser.add_argument('-v',
#                         '--verbose',
#                         help='verbose output.',
#                         action='store_true')
#     parser.add_argument('-a',
#                         '--all',
#                         help='output all possible solutions.',
#                         action='store_true')
#     parser.add_argument('-b',
#                         '--brief',
#                         help=('brief output:'
#                               ' only outputs variables assigned true.'),
#                         action='store_true')
#     parser.add_argument('--starting_with',
#                         help=('only output variables with names'
#                               ' starting with the given string.'),
#                         default='')
#     parser.add_argument('--iterative',
#                         help='use the iterative algorithm.',
#                         action='store_const',
#                         dest='solver',
#                         default=recursive_sat,
#                         const=iterative_sat)
#     parser.add_argument('-i',
#                         '--input',
#                         help='read from given file instead of stdin.',
#                         type=FileType('r'),
#                         default=stdin)
#     parser.add_argument('-o',
#                         '--output',
#                         help='write to given file instead of default stdout.',
#                         type=FileType('w'),
#                         default=stdout)
#     return parser.parse_args()


if __name__ == '__main__':
    main()
