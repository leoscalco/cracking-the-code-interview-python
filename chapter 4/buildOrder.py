UNVISITED = 0
VISITED = 1
VISITING = 2

class Project:
    def __init__(self, name):
        self.children = []
        self.map = {}
        self.name = name
        self.dependencies = 0

    def addNeighbor(self, node):
        if not node.name in self.map:
            self.children.append(node)
            self.map[node.name] = node
            node.dependencies+=1

class Graph:
    def __init__(self):
        self.nodes = []
        self.map = {}

    def getOrCreateNode(self, name):
        if not name in self.map:
            node = Project(name)
            self.nodes.append(node)
            self.map[name] = node

        return self.map[name]

    def addEdge(self, startName, endName):
        start = self.getOrCreateNode(startName)
        end = self.getOrCreateNode(endName)
        start.addNeighbor(end)

def buildGraph(projects, dependencies):
    g = Graph()
    for p in projects:
        g.getOrCreateNode(p)

    for d in dependencies:
        g.addEdge(d[0], d[1])

    return g

def addNonDependent(order, projects, offset):
    for p in projects:
        if p.dependencies == 0:
            order[offset] = p
            offset+=1
    return offset

def orderProjects(projects):
    order = [None] * len(projects)

    endOfList = addNonDependent(order, projects, 0)

    toBeProcessed = 0
    while toBeProcessed < len(order):
        print "order "
        print order
        current = order[toBeProcessed]

        if(current == None):
            return None

        children = current.children
        for c in children:
            c.dependencies -= 1

        endOfList = addNonDependent(order, children, endOfList)
        toBeProcessed+=1

    return order

def findBuildOrder(projects, dependencies):
    g = buildGraph(projects, dependencies)
    return orderProjects(g.nodes)


projects = 'a b c d e f'.split()
dependencies = 'ad fb bd fa dc'.split()

for o in findBuildOrder(projects, dependencies):
    print o.name