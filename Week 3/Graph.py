class Node:
    def __init__(self, state):
        self.state = state
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, action, cost, next_node):
        self.action = action
        self.cost = cost
        self.next_node = next_node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, state):
        if state not in self.nodes:
            self.nodes[state] = Node(state)
        return self.nodes[state]

    def add_edge(self, state_from, action, cost, state_to):
        node_from = self.add_node(state_from)
        node_to = self.add_node(state_to)
        edge = Edge(action, cost, node_to)
        node_from.add_edge(edge)

    def get_node(self, state):
        return self.nodes.get(state, None)

def read_graph_from_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()
        nodes_section = False
        edges_section = False

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("graph"):
                graph_name = line.split()[1]
                nodes_section = False
                edges_section = False

            elif line.startswith("nodes"):
                nodes_section = True
                edges_section = False

            elif line.startswith("edges"):
                nodes_section = False
                edges_section = True

            elif nodes_section:
                nodes = line.split()
                for node in nodes:
                    graph.add_node(node)

            elif edges_section:
                parts = line.split()
                if len(parts) == 2:
                    state_from, state_to = parts
                    graph.add_edge(state_from, 'edge', 1, state_to)
                elif len(parts) == 3:
                    state_from, state_to, cost = parts
                    graph.add_edge(state_from, 'edge', int(cost), state_to)

    return graph

filename = "graph.txt"
graph = read_graph_from_file(filename)

