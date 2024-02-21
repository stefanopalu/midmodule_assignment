"""recursive floyd warshall"""

INF = 99999

def floydwarshall_recursive(graph):
    """enclosing function that uses the recursive function"""
    v = len(graph)
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    def shortest_path(start, end, inter):
        """nested recursive function that calculates the shortest path"""
        if inter >= 0:
            start_end = shortest_path(start, end, inter - v)
            start_inter = shortest_path(start, inter, inter - v)
            inter_end = shortest_path(inter, end, inter - v)
        else:
            return distance[start][end]
        return min(start_end, start_inter + inter_end)

    for inter in range(v):
        for start in range(v):
            for end in range(v):
                if start == end or start == inter or end == inter:
                    continue
                distance[start][end] = shortest_path(start, end, inter)
    return distance
