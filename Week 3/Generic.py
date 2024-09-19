from Graph import Graph
from Graph import Edge


class SearchProblem:
    def __init__(self, graph, start_state, goal_state):
        self.graph = graph
        self.start_state = start_state
        self.goal_state = goal_state

    def start_state(self):
        return self.start_state

    def is_end(self, state):
        return state == self.goal_state

    def successors(self, state):
        node = self.graph.get_node(state)
        return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]


g = Graph()
s = SearchProblem()