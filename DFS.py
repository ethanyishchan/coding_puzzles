def dfs(graph,start):
    path = []
    stack = [start]
    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        for w in reversed(graph[v]):
            if w not in path:
                stack.append(w)
    return path



class Node:
    def __init__(self, adj_nodes, visited = False):
        self.adj_nodes = adj_nodes
        self.visited = visited

G = {
    'a' : ['b','c','d'],
    'b' : ['d'],
    'c' : ['d'],
    'd' : [],
    'e' : []
    }

G_unmarked = ['a','b','c','d','e']

def DFS_G (G, G_marked):
    #if not all are visited
    while len(G_unmarked):
        DFS_U (G_unmarked[0], G, G_marked)

def adj (node):
    return node.adj_nodes

def DFS_U (node, G, G_marked):
    #mark as visited
    print node
    print G_marked
    G_marked.pop(node)
    print G_marked
    print " "

    for v in G[node]:
        DFS_U(v, G, G_marked)

DFS_G (G, G_unmarked)






