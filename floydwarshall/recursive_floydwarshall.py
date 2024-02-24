"""recursive floyd warshall"""

INF = 99999

def floydwarshall_recursive(graph):
    """enclosing function that uses the recursive function"""
    v = len(graph)
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    def shortest_path(start, end, inter):
        """nested recursive function that calculates the shortest path"""
        if inter >= 0:
            # if the stopping condition isn't meet the function call itself to calculate
            # the distance between the start and the end node, the one between the start
            # node and the intermediate node  and the one between the intermediate node
            # and the end node
            start_end = shortest_path(start, end, inter - v)
            start_inter = shortest_path(start, inter, inter - v)
            inter_end = shortest_path(inter, end, inter - v)
        else:
            # return distance
            return distance[start][end]
        # return the lower value between start_end and the sum of the other two
        return min(start_end, start_inter + inter_end)

    for inter in range(v):
        for start in range(v):
            for end in range(v):
                # skip unnecessary steps
                if start == end or start == inter or end == inter:
                    continue
                distance[start][end] = shortest_path(start, end, inter)
    return distance
