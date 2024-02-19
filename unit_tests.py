"""unit test"""

import random
import unittest
from floydwarshall.recursive_floydwarshall import floydwarshall_recursive
from floydwarshall.imperative_floydwarshall import floydwarshall_imperative

INF = 99999

def generate_graph():
    """random graph generator"""
    # generate a random number of vertexes between 1 and 10
    vertex_n = random.randint(1,10)
    # establish a percentage of values that will be inf
    inf_percentage = random.randint(0,100)
    # calculate how many values that will be numbers
    n_numbers = int(vertex_n**2 * (inf_percentage/100))

    # generate random numbers and inf_values and combine the two lists
    numbers_values = [random.randint(0,100) for _ in range(n_numbers)]
    inf_values = [INF] * (vertex_n**2 - n_numbers)
    all_values = numbers_values + inf_values

    # shuffle the combined list
    random.shuffle(all_values)

    # create a graph from the shuffled combined list
    graph = [all_values[i:i+vertex_n] for i in range(0, len(all_values), vertex_n)]

    return graph

graph1 = generate_graph()
graph2 = generate_graph()
graph3 = generate_graph()

#Unit Tests

class TestFloyd(unittest.TestCase):
    """unit tests"""
    def test_floyd_1(self):
        self.assertEqual(floydwarshall_recursive(graph1),
                         floydwarshall_imperative(graph1),
                         "Output incorrect")

    def test_floyd_2(self):
        self.assertEqual(floydwarshall_recursive(graph2),
                         floydwarshall_imperative(graph2),
                         "Output incorrect")
        
    def test_floyd_3(self):
        self.assertEqual(floydwarshall_recursive(graph3),
                         floydwarshall_imperative(graph3),
                         "Output incorrect")

if __name__ == '__main__':
    unittest.main()
