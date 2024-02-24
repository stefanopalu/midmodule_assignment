"""unit tests"""

import unittest
from floydwarshall.recursive_floydwarshall import floydwarshall_recursive
from floydwarshall.imperative_floydwarshall import floydwarshall_imperative
from floydwarshall.randomgraph_generator import generate_graph

# generate four graph with our function to test our recursive function against the imperative one

#Unit Tests
class TestFloyd(unittest.TestCase):
    """unit tests"""
    def test_floyd_1(self):
        """compare the two functions with a small graph with 3 vertexes"""
        graph = generate_graph(3,50)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

    def test_floyd_2(self):
        """compare the two functions with a graph with a high percentage of INF values"""
        graph = generate_graph(5,90)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

    def test_floyd_3(self):
        """compare the two functions with a graph with a low percentage of INF values"""
        graph = generate_graph(5,10)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

    def test_floyd_4(self):
        """compare the two functions with a large graph with 100 vertexes"""
        graph = generate_graph(100,60)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

if __name__ == '__main__':
    unittest.main()
