from BestSearch import BestFirstSearch



def bfs_priority(state, cost):
 return cost


def uniform_search_cost(problem):
    bfs_search = BestFirstSearch(problem, bfs_priority)
    result = bfs_search.search()
    return result
