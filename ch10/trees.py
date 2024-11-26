#
#  file:  trees.py
#
#  Tree algorithms (binary search trees)
#
#  RTK, 17-Jul-2023
#  Last update:  12-Aug-2023
#
################################################################

#
#  Math section (graphs ala Chapter 9):
#

#  DFS to locate a spanning tree (G is Fig 9-1, W is G with weights)
G = [{1,2}, {0,3,4}, {0,5}, {1}, {1,5}, {2,4}]
W = [{(1,2),(2,1)}, {(0,2),(3,1),(4,4)}, {(0,1),(5,3)}, {(1,1)}, {(1,4),(5,2)}, {(2,3),(4,2)}]

#  Complete graphs
K3 = [{1,2}, {0,2}, {0,1}]
K4 = [{1,2,3}, {0,2,3}, {0,1,3}, {0,1,2}]
K5 = [{1,2,3,4}, {0,2,3,4}, {0,1,3,4}, {0,1,2,4}, {0,1,2,3}]
K7 = [{1,2,3,4,5,6},{0,2,3,4,5,6},{0,1,3,4,5,6},{0,1,2,4,5,6},{0,1,2,3,5,6},{0,1,2,3,4,6},{0,1,2,3,4,5}]

def SpanningTree(graph, start=0):
    """Return a spanning tree for an unweighted graph"""
    def DFS(graph, vertex, visited, spanning):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                spanning[vertex].add(neighbor)
                spanning[neighbor].add(vertex)
                DFS(graph, neighbor, visited, spanning)

    n = len(graph)
    visited = [False] * n
    spanning = [set() for i in range(n)]
    DFS(graph, start, visited, spanning)
    return spanning


#
#  Kirchhoff's Matrix-Tree theorem
#
def NumberOfSpanningTrees(graph):
    """Return the number of spanning trees in a graph"""

    def LaplacianMatrix(graph):
        """Generate the Laplacian matrix as a list of lists"""
        n = len(graph)
        L = [[0] * n for i in range(n)]  # n by n
        for i in range(n):
            L[i][i] = len(graph[i])
            for j in graph[i]:
                L[i][j] = -1
        return L

    def Determinant(matrix):
        """Recursively calculate the determinant of a square matrix"""
        n = len(matrix)
        if (n == 1):
            return matrix[0][0]
        det = 0
        for c in range(n):
            submatrix = [row[:c] + row[c+1:] for row in matrix[1:]]
            sign = 1 if c % 2 == 0 else -1
            det += sign * matrix[0][c] * Determinant(submatrix)
        return det

    L = LaplacianMatrix(graph)
    L_prime = [row[:-1] for row in L[:-1]]
    return Determinant(L_prime)


#
#  Prim's MST
#
def Prim(graph):
    """Return the minimum spanning tree for the given weighted graph"""
    n = len(graph)        # number of nodes
    visited = [False]*n   # visited nodes
    googol = 1e100        # 'infinity'
    dist = [googol]*n     # track smallest weights (ala Dijkstra in Ch 9)
    parent = [None]*n     # parent of each node (to build the MST)

    #  Start with node 0
    dist[0] = 0

    for i in range(n):
        #  Find the unvisited node with the minimum distance
        m, u = googol, 0
        for v in range(n):
            if (not visited[v]) and (dist[v] < m):
                m, u = dist[v], v

        #  Mark the vertex as visited
        visited[u] = True

        #  Examine the neighbors of u
        for neighbor, weight in graph[u]:
            if (not visited[neighbor]) and (weight < dist[neighbor]):
                dist[neighbor] = weight
                parent[neighbor] = u

    #  Build the MST as an adjacency list
    mst = [set() for i in range(n)]
    for v in range(1, n):
        u = parent[v]
        for i,w in graph[v]:
            if (i == u):
                weight = w
        mst[u].add((v, weight))  # undirected graphs have edges from
        mst[v].add((u, weight))  # u to v and v to u
    return mst


#
#  Code section:
#

#  A binary tree node
class Node:
    """A single node"""
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

#  Add to the tree
def Insert(key, value=None, node=None):
    if (key < node.key):
        if (node.left is None):
            node.left = Node(key, value)
        else:
            Insert(key, value, node=node.left)
    else:
        if (node.right is None):
            node.right = Node(key, value)
        else:
            Insert(key, value, node=node.right)

#  Find a key in the tree
def Search(key, node=None):
        if (key < node.key):
            if (node.left is None):
                return False, None
            return Search(key, node=node.left)
        elif (key > node.key):
            if (node.right is None):
                return False, None
            return Search(key, node=node.right)
        else:
            return True, node.value

#  Traversals
def Preorder(root, leaves=False):
    """Pre-order traversal"""
    def preorder(node, traversal, leaves=False):
        """node > left > right"""
        if (node):
            if (leaves):
                if (node.left is None) and (node.right is None):
                    traversal.append(node.value if node.value is not None else node.key)
            else:
                traversal.append(node.value if node.value is not None else node.key)
            preorder(node.left, traversal, leaves=leaves)
            preorder(node.right, traversal, leaves=leaves)
        return traversal
    traversal = []
    preorder(root, traversal, leaves=leaves)
    return traversal

def Inorder(root):
    """In-order traversal"""
    def inorder(node, traversal):
        """left > node > right"""
        if (node):
            inorder(node.left, traversal)
            traversal.append(node.value if node.value is not None else node.key)
            inorder(node.right, traversal)
        return traversal
    traversal = []
    inorder(root, traversal)
    return traversal

def Postorder(root):
    """Post-order traversal"""
    def postorder(node, traversal):
        """left > right > node"""
        if (node):
            postorder(node.left, traversal)
            postorder(node.right, traversal)
            traversal.append(node.value if node.value is not None else node.key)
        return traversal
    traversal = []
    postorder(root, traversal)
    return traversal

def BreadthFirst(root):
    queue = [root]
    traversal = []
    while (queue):
        node = queue.pop(0)
        traversal.append(node.value if node.value is not None else node.key)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return traversal

def Leaves(root):
    return Preorder(root, leaves=True)

#  Build a binary search tree from data
def BuildTree(n):
    """Create a tree from a list"""
    if (type(n[0]) is tuple) or (type(n[0]) is list):
        tree = Node(n[0][0],n[0][1])
        [Insert(i[0],i[1],tree) for i in n[1:]]
    else:
        tree = Node(n[0])
        [Insert(i, node=tree) for i in n[1:]]
    return tree

#  Build an abstract syntax tree by hand
ast = Node("-")
ast.left = Node("*")
ast.left.left = Node("+")
ast.left.left.left = Node("2")
ast.left.left.right = Node("a")
ast.left.right = Node("b")
ast.right = Node("*")
ast.right.left = Node("4")
ast.right.right = Node("c")

#  Evaluating an AST using post-order traversal and a stack
def Evaluate(ast, a=1, b=2, c=3):
    """Evaluate an ast using a stack"""
    stack = []
    for token in Postorder(ast):
        if (token in ["+","-","*","/"]):
            y,x = stack.pop(), stack.pop()
            stack.append(eval(str(x) + token + str(y)))
        else:
            stack.append(eval(token))
    print(stack[-1])

#
#  Animals game
#
def Animals(root=None):
    """Play a game of animals"""
    def PlayRound(node, parent=None):
        learned = False
        if (node.left is None) and (node.right is None):
            #  Leaf nodes are animal guesses
            answer = input("Is it a " + node.key + "? (yes/no): ").lower()
            if (answer == "yes"):
                print("I won!")
            else:
                #  Computer lost, get new animal info
                learned = True
                animal = input("I give up.  What animal were you thinking of? ")
                question = input("What question would distinguish a " + animal + " from a " + node.key + "? ")
                answer = input("What is the correct answer for a " + animal + "? (yes/no) ").lower()
                animal_node = Node(animal)
                question_node = Node(question)
                question_node.left = animal_node if (answer == "yes") else node
                question_node.right = node if (answer == "yes") else animal_node
                if (parent):
                    if (parent.left == node):
                        parent.left = question_node
                    else:
                        parent.right = question_node
                return question_node, learned
        else:
            #  Non-leaf nodes are questions
            answer = input(node.key + " (yes/no): ").lower()
            if (answer == "yes"):
                node.left, learned = PlayRound(node.left, node)
            else:
                node.right, learned = PlayRound(node.right, node)
        return node, learned

    #  Play the game
    if (root is None):
        root = Node("mosquito")
    while (True):
        input("Think of an animal and press 'enter' when ready... ")
        root, learned = PlayRound(root)
        if (input("Play again? (yes/no): ").lower() != "yes"):
            break
        if (learned):
            print("I now know %d animals!" % len(Leaves(root)))
    print("Goodbye!")
    return root  # return the tree

# end trees.py

