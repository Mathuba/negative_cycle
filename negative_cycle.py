#Uses python3

import sys


def add_edge(graph, vert1, vert2, weight):
    """Build directed graph with edge weights.

    This directed graph may also contain negative weights.
    """

    weighted_edge = [vert2, weight]
    if vert1 in graph:
        graph[vert1].append(weighted_edge)
    else:
        graph[vert1] = weighted_edge

def negative_cycle(adj, cost):
    #write your code here
    return 0


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    for _ in range(m):
        vert1, vert2, weight = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2, weight)
    # print(negative_cycle(adj, cost))
    print(graph)
