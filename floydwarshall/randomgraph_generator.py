"""graph generator with random numbers"""

import random

INF = 99999

def generate_graph(vertex_n, inf_percentage):
    """function to create a random graph"""    
    # generate a random number of vertices between 2 and 10
    if vertex_n < 3:
        raise ValueError ("The number of vertexes must be greater than 3")
    # establish a percentage of values that will be inf
    if inf_percentage < 0 or inf_percentage > 100:
        raise ValueError ("The percentage of INF values must be bewtween 0 and 100")
    # calculate how many values will be numbers
    n_numbers = int(vertex_n**2 * (inf_percentage/100))

    # generate random distances and inf_values and combine the two lists
    distances = [random.randint(1,1000) for _ in range(n_numbers)]
    inf_distances = [INF] * (vertex_n**2 - n_numbers)
    all_distances = distances + inf_distances

    # shuffle the combined list
    random.shuffle(all_distances)

    # create a weighted distance graph from the shuffled combined list
    # if i and j have the same value it will be set to zero (the distance of a vertex to itself)
    graph = [[INF] * vertex_n for _ in range(vertex_n)]
    index = 0
    for row in range(vertex_n):
        for col in range(vertex_n):
            if row != col:
                graph[row][col] = all_distances[index]
                index += 1
            else:
                graph[row][col] = 0

    return graph
