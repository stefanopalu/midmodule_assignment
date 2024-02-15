"""Python3 Program for Floyd Warshall Algorithm"""
V = 4
INF = 99999

def floydWarshall(graph):
    """Python3 Program for Floyd Warshall Algorithm"""

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        # pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    return dist
