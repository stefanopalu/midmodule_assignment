"""graph generator with random numbers"""

import random

INF = 99999

def generate_graph(vertex_num, inf_percentage):
    """Function to create a random graph"""    
    # Handling errors in vertex number and inf values percentage
    if vertex_num < 3:
        raise ValueError ("The number of vertexes must be greater than 3")
    if inf_percentage < 0 or inf_percentage > 100:
        raise ValueError ("The percentage of INF values must be bewtween 0 and 100")

    # Calculate how many values will be numbers
    numbers_num = int(vertex_num**2 * (inf_percentage/100))

    # Generate random distances and inf_values and combine the two lists
    distances = [random.randint(1,1000) for _ in range(numbers_num)]
    inf_distances = [INF] * (vertex_num**2 - numbers_num)
    all_distances = distances + inf_distances

    # Shuffle the combined list
    random.shuffle(all_distances)

    # Create a weighted distance graph from the shuffled combined list
    # If row and col have the same value it will be set to zero (the distance of a vertex to itself)
    graph = [[INF] * vertex_num for _ in range(vertex_num)]
    index = 0
    for row in range(vertex_num):
        for col in range(vertex_num):
            if row != col:
                graph[row][col] = all_distances[index]
                index += 1
            else:
                graph[row][col] = 0

    return graph
