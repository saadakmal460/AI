from Graph import Graph

class TransportationProblem:
    def __init__(self, N):
        self.N = N
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        for state in range(1, self.N + 1):
            self.graph.add_node(state)
            if state + 1 <= self.N:
                self.graph.add_edge(state, 'walk', 1, state + 1)
            if state * 2 <= self.N:
                self.graph.add_edge(state, 'tram', 2, state * 2)

    def start_state(self):
        return 1

    def is_end(self, state):
        return state == self.N

    def successors(self, state):
        node = self.graph.get_node(state)
        return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]

problem = TransportationProblem(N=10)
