from BestSearch import BestFirstSearch
from Transportation import TransportationProblem


def bfs_priority(state, cost):
 return cost


def uniform_search_cost(problem):
    bfs_search = BestFirstSearch(problem, bfs_priority)
    result = bfs_search.search()
    return result



problem = TransportationProblem(N=10)

result = uniform_search_cost(problem)
print(result)