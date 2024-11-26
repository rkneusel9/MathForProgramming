#
#  file:  graphs.py
#
#  Graph routines
#
#  RTK, 21-Jun-2023
#  Last update:  16-Jul-2023
#
################################################################

#  N.B. directed graphs must have positive weights > 0 (this is just a pedagogical library, after all)

#  Three isomorphic graphs, first is left of Figure 9-1
A = [{1,2},{0,3,4},{0,5},{1},{1,5},{2,4}]
B = [{3},{4,5},{3,4},{0,2,5},{1,2},{1,3}]
C = [{1,2,5},{0,3},{0},{1,4},{3,5},{0,4}]

#  A graph with the same number of nodes that is not isomorphic to A,B,C
D = [{1},{0,4},{4,5},{4},{1,2,3},{2}]

#  A directed graph (right of Figure 9-1)
E = [{1},{3},{0,5},set(),{1,5},set()]

#  Weighted undirected graph (weighted version of A)
F = [{(1,3),(2,2)}, {(0,3),(3,2),(4,6)}, {(0,2),(5,5)}, {(1,3)}, {(1,6),(5,2)}, {(2,5),(4,2)}]

#  Weighted directed graph (weighted version of E)
G = [{(1,3)},{(3,2)},{(0,2),(5,5)},set(),{(1,6),(5,2)},set()]

#  Star graph
S = [{1,2,3,4},{0,5},{0,6},{0,7},{0,8},{1,9},{2,10},{3,11},{4,12},{5},{6},{7},{8}]

#  Shortest path examples
U = [{1,2,3},{0,4},{0,5},{0,5,6},{1,6},{2,3,7},{3,4,7},{5,6}]  # undirected, unweighted
T = [{1,2,3},set(),set(),{5,6},{1,6},{2,7},{7},set()]          # directed, unweighted

#  undirected, weighted
W = [{(1,2),(2,3),(3,2)},{(0,2),(4,1)},{(0,3),(5,7)},{(0,2),(5,4),(6,3)},{(1,1),(6,1)},{(2,7),(3,4),(7,9)},{(3,3),(4,1),(7,3)},{(5,9),(6,3)}]

#  directed, weighted
V = [{(1,2),(2,3),(3,2)},set(),set(),{(5,4),(6,3)},{(1,1),(6,1)},{(2,7),(7,9)},{(7,3)},set()]

#  Topological sorting
dress = [{6},{3},{4,5,9},{4,6},set(),{7},set(),set(),set(),set()]
cycle = [{1,2},{4},{3,4},{0,4},set()]  # 0 -> 2 -> 3 -> 0
nocycle = [{1,2},{4},{4},{0,4},set()]  # remove 2 -> 3 edge

#  Utility functions
def ListToMatrix(lst):
    """Convert an adjacency list to a matrix"""
    n = len(lst)
    mat = []
    [mat.append([0]*n) for i in range(n)]
    for i in range(n):
        for j in lst[i]:
            if type(j) is tuple:
                if (j[0] is None):
                    continue
                mat[i][j[0]] = j[1]
            else:
                if (j is None):
                    continue
                mat[i][j] = 1
    return mat

def MatrixToList(mat, force=False):
    """Convert an adjacency matrix to a list, force weighted if True"""
    n = len(mat)
    lst = []
    for i in range(n):
        l = set()
        for j in range(n):
            v = mat[i][j]
            if (v == 1):
                if (force):
                    l.add((j,1))
                else:
                    l.add(j)
            elif (v > 1):
                l.add((j,v))
        lst.append(l)
    return lst


#
#  Traversals only
#
def DepthFirst(graph, node, visited=None, weighted=False):
    """Depth-first traversal of a graph"""
    if visited is None:
        visited = []
    visited.append(node)
    if (weighted):
        #  weighted
        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                DepthFirst(graph, neighbor, visited=visited, weighted=weighted)
    else:
        #  unweighted
        for neighbor in graph[node]:
            if neighbor not in visited:
                DepthFirst(graph, neighbor, visited=visited, weighted=weighted)
    return visited


def BreadthFirst(graph, start, weighted=False):
    """Breadth-first traveral of a graph"""
    visited, queue = [start], [start]
    while queue:
        node = queue.pop(0) 
        if (weighted):
            #  weighted
            for neighbor,weight in graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        else:
            #  unweighted
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
    return visited

#
#  Searches (unweighted graphs only):
#

#  Node data for graphs A-E
people = {
    0: ['Drofo', 'hafling'],
    1: ['Aranorg', 'human'],
    2: ['Yowen', 'human'],
    3: ['Fangald', 'wizard'],
    4: ['Lelogas', 'elf'],
    5: ['Milgi', 'dwarf'],
}

def DepthFirstSearch(graph, node, visited=None, name=None, data=None):
    """Depth-first search of a graph for a name"""
    if (visited is None):
        visited= []
    if data[node][0] == name:
        return True, data[node][1]
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            found, type = DepthFirstSearch(graph, neighbor, visited=visited, name=name, data=data)
            if (found):
                return found, type
    return False, None


def BreadthFirstSearch(graph, start, name=None, data=None):
    """Breadth-first search of a graph for a name"""
    visited, queue = [start], [start]
    while queue:
        node = queue.pop(0) 
        if (data[node][0] == name):
            return True, data[node][1]
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return False, None


#
#  Paths:
#
def ShortestPath(graph, start, end):
    """BFS to locate the shortest path in an unweighted graph"""
    visited, queue = [start], [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if (node == end):
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(path + [neighbor])
    return []


def Dijkstra(graph, start, end=None):
    """Find the shortest path between two nodes in a weighted graph"""

    def AllPaths(shortest_path):
        paths = []
        for i in range(len(shortest_path)):
            path = []
            while i is not None:
                path.append(i)
                i = shortest_path[i]
            path.reverse()
            paths.append(path)
        return paths

    #  distances from start to each node, updated as graph traversed
    googol = 1E100  # assume no distance greater than a googol
    n = len(graph)  # number of nodes in the graph
    distances = [googol] * n
    distances[start] = 0  # distance to start from start

    #  initialize a list to store the shortest path
    shortest_path = [None] * n

    #  the set of unvisited nodes
    unvisited = {i for i in range(n)}
    current_node = start

    while True:
        #  check all the neighbors of the current node
        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight

            #  update the neighbor's distance if a shorter path is found
            if (new_distance < distances[neighbor]):
                distances[neighbor] = new_distance
                shortest_path[neighbor] = current_node

        #  mark the current node as visited
        unvisited.remove(current_node)

        #  all nodes considered or end node found
        if (end == None):
            if (not unvisited):
                break
        else:
            if (not unvisited) or (current_node == end):
                break

        #  the next node is the unvisited node with the smallest distance
        k = [i for i in unvisited]
        d = [distances[i] for i in unvisited]
        current_node = k[d.index(min(d))]

    #  return the path and total distance
    if (end == None):
        return AllPaths(shortest_path), distances
    else:
        path = []
        while end is not None:
            path.append(end)
            end = shortest_path[end]
        path.reverse()
        if distances[path[-1]] < googol:
            return path, distances[path[-1]]
        return [], 0


#
#  Topological sorting:
#
def TopologicalSort(graph, weighted=False):
    """Return a topological sort of a DAG (assumed valid)"""

    def DFS(graph, node, visited, result, weighted=False):
        visited.add(node)
        if (not weighted):
            for neighbor in graph[node]:
                if (neighbor not in visited):
                    DFS(graph, neighbor, visited, result, weighted=weighted)
        else:
            for neighbor, weight in graph[node]:
                if (neighbor not in visited):
                    DFS(graph, neighbor, visited, result, weighted=weighted)
        result.insert(0, node)

    visited = set()
    result = []
    for node in range(len(graph)):
        if (node not in visited):
            DFS(graph, node, visited, result, weighted=weighted)
    return result


#
#  Graph isomorphism:
#
def Isomorphic(g1, g2):
    """Brute force check if two undirected, unweighted graphs are isomorphic"""    
    from combinatorics import Permutations

    #  isomorphic graphs must have the same number of vertices
    if (len(g1) != len(g2)):
        return False

    # g2 as a sorted list of vertices with each
    # vertex list sorted as well
    g2_sorted = sorted([sorted(list(v)) for v in g2])

    for perm in Permutations(list(range(len(g1)))):
        #  map the vertices of g1 to the permutation
        mapping = [perm[i] for i in range(len(perm))]

        #  rebuild g1 according to the mapping
        g1_perm = []
        for v in range(len(g1)):
            t = []
            for n in g1[v]:
                t.append(mapping[n])
            g1_perm.append(sorted(t))
        g1_perm.sort()

        #  if the same, then there is a permutation that works
        if (g1_perm == g2_sorted):
            return True, perm

    #  no permutation works, not isomorphic
    return False, None


