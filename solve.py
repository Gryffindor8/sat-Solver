from collections import defaultdict

neg = '~'


class dir_graph:
    def __init__(self):
        # create an empty directed graph, represented by a dictionary
        #  The dictionary consists of keys and corresponding lists
        #  Key = node u , List = nodes, v, such that (u,v) is an edge
        self.graph = defaultdict(set)
        self.nodes = set()

    # Function that adds an edge (u,v) to the graph
    #  It finds the dictionary entry for node u and appends node v to its list
    # performance: O(1)
    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.nodes.add(u)
        self.nodes.add(v)

    # Function that outputs the edges of all nodes in the graph
    #  prints all (u,v) in the set of edges of the graoh
    # performance: O(m+n) m = #edges , n = #nodes
    def print(self):
        edges = []
        # for each node in graph
        for node in self.graph:
            # for each neighbour node of a single node
            for neighbour in self.graph[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        return edges


class two_cnf:
    def __init__(self):
        self.con = []

    # adds a clause to the CNF
    # performance O(1)
    def add_clause(self, clause):
        if len(clause) <= 2:
            self.con.append(clause)
        else:
            print("error: clause contains > 2 literals")

    # returns a set of all the variables in the CNF formula
    def get_variables(self):
        vars = set()
        for clause in self.con:
            for literal in clause:
                vars.add(literal)
        return vars

    def print(self):
        print(self.con)


# helper function that applies the double negation rule to a formula
#   the function removes all occurrences ~~ from the formula
def double_neg(formula1):
    return formula1.replace((neg + neg), '')


# Function that performs Depth First Search on a directed graph
# O(|V|+|E|)
def DFS(dir_graph1, visited, stack, scc):
    for node in dir_graph1.nodes:
        if node not in visited:
            explore(dir_graph1, visited, node, stack, scc)


# DFS helper function that 'explores' as far as possible from a node
def explore(dir_graph2, visited, node, stack, scc):
    if node not in visited:
        visited.append(node)
        for neighbour in dir_graph2.graph[node]:
            explore(dir_graph2, visited, neighbour, stack, scc)
        stack.append(node)
        scc.append(node)
    return visited


# Function that generates the transpose of a given directed graph
# Performance O(|V|+|E|)
def transpose_graph(d_graph):
    t_graph = dir_graph()
    # for each node in graph
    for node in d_graph.graph:
        # for each neighbour node of a single node
        for neighbour in d_graph.graph[node]:
            t_graph.addEdge(neighbour, node)
    return t_graph


# Function that finds all the strongly connected components in a given graph
# Implementation of Kosaraju’s algorithm
# Performance O(|V|+|E|) for a directed graph G=(V,E)
# IN : directed graph, G
# OUT: list of lists containing the strongly connected components of G
def strongly_connected_components(dir_graph1):
    stack = []
    sccs = []
    DFS(dir_graph1, [], stack, [])
    t_g = transpose_graph(dir_graph1)
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            scc.append(node)
            explore(t_g, visited, node, [], scc)
            sccs.append(scc)
    return sccs


def find_contradiction(sccs):
    for component in sccs:
        for literal in component:
            for other_literal in component[component.index(literal):]:
                if other_literal == double_neg(neg + literal):
                    return True
    return False


# Function that determines if a given 2-CNF is Satisfiable or not
def two_sat_solver(two_cnf_formula):
    print("Checking if the following 2-CNF is Satisfiable in linear time ")
    two_cnf_formula.print()
    graph = dir_graph()
    for clause in two_cnf_formula.con:
        if len(clause) == 2:
            u = clause[0]
            v = clause[1]
            graph.addEdge(double_neg(neg + u), v)
            graph.addEdge(double_neg(neg + v), u)
        else:
            graph.addEdge(double_neg(neg + clause[0]), clause[0])
    if not find_contradiction(strongly_connected_components(graph)):
        print("2-CNF Satisfiable")
    else:
        print("2-CNF not Satisfiable")


# [a, b, a, c, ~b, d]
# ======= 2-CNF setup =======
formula = two_cnf()

formula.add_clause(['a', 'b', 'c'])
formula.add_clause(['~a', 'b', 'm'])
formula.add_clause(['a', '~b', 'c'])
formula.add_clause(['~a', '~b', 'd'])
two_sat_solver(formula)
