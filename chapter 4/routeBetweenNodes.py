from collections import deque
UNVISITED = 0
VISITED = 1
VISITING = 2

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.state = UNVISITED

    def addChildren(self, node):
        self.children.append(node)

    def getChildren(self):
        return self.children

class Graph:
    def __init__(self):
        self.nodes = []
        self.adjacent = {}

    def addNode(self, node):
        self.nodes.append(node)
        self.adjacent[node.name] = node.children

    def getNodes(self):
        return self.nodes

def search(g, s_node, e_node):
    if (s_node == e_node):
        return True
    # queue
    q = deque()

    # for node in g.getNodes():
    #     node.state = UNVISITED ja

    s_node.state = VISITING
    q.append(s_node)

    # u = Node(None)
    while(len(q) > 0):
        u = q.popleft()
        if (u != None):
            for v in u.getChildren():
                if v.state == UNVISITED:
                    if v == e_node:
                        return True
                    else:
                        v.state = VISITING
                        q.append(v)
            u.state = VISITED
    return False

g = Graph()

n1 = Node('s')
n2 = Node('r')
n3 = Node('t')

n1.addChildren(n2)
n1.addChildren(n3)
n2.addChildren(n3)
# n3.addChildren(n1)

g.addNode(n1)
g.addNode(n2)
g.addNode(n3)

print search(g, n3, n2)