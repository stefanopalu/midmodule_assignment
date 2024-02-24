"""Recursive floyd warshall"""

INF = 99999

def floydwarshall_recursive(graph):
    """Enclosing function that uses the recursive function"""
    v = len(graph)
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    def shortest_path(start, end, inter):
        """Nested recursive function that calculates the shortest path"""
        if inter >= 0:
            # If the stopping condition isn't meet the function call itself to calculate
            # the distance between the start and end nodes, the one between the start and
            # the intermediate node and the one between the intermediate and the end node
            start_end = shortest_path(start, end, inter - v)
            start_inter = shortest_path(start, inter, inter - v)
            inter_end = shortest_path(inter, end, inter - v)
        else:
            # Return distance
            return distance[start][end]
        # Return the lower value between start_end and the sum of the other two
        return min(start_end, start_inter + inter_end)

    for inter in range(v):
        for start in range(v):
            for end in range(v):
                # Skip unnecessary steps
                if start == end or start == inter or end == inter:
                    continue
                distance[start][end] = shortest_path(start, end, inter)
    return distance
