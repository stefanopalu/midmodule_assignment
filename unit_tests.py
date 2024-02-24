"""Unit tests"""

import unittest
from floydwarshall.recursive_floydwarshall import floydwarshall_recursive
from floydwarshall.imperative_floydwarshall import floydwarshall_imperative
from floydwarshall.randomgraph_generator import generate_graph

# Generate four graph with our function and test our recursive function against the imperative one

class TestFloyd(unittest.TestCase):
    """Unit tests"""
    def test_floyd_1(self):
        """Compare the two functions with a small graph with 3 vertexes"""
        graph = generate_graph(3,50)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

    def test_floyd_2(self):
        """Compare the two functions with a sparse graph with a high percentage of INF values"""
        graph = generate_graph(10,95)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

    def test_floyd_3(self):
        """Compare the two functions with a dense graph with a low percentage of INF values"""
        graph = generate_graph(10,5)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

    def test_floyd_4(self):
        """Compare the two functions with a large graph with 100 vertexes"""
        graph = generate_graph(100,60)
        self.assertEqual(floydwarshall_recursive(graph),
                         floydwarshall_imperative(graph),
                         "Output incorrect")

if __name__ == '__main__':
    unittest.main()
