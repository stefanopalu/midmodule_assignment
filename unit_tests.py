"""unit tests"""

import unittest
from floydwarshall.recursive_floydwarshall import floydwarshall_recursive
from floydwarshall.imperative_floydwarshall import floydwarshall_imperative
from floydwarshall.randomgraph_generator import generate_graph

# generate four graph with our function to test our recursive function against the imperative one
graph1 = generate_graph()
graph2 = generate_graph()
graph3 = generate_graph()
graph4 = generate_graph()

#Unit Tests
class TestFloyd(unittest.TestCase):
    """unit tests"""
    def test_floyd_1(self):
        """compare the recursive and imperative function with the first graph"""
        self.assertEqual(floydwarshall_recursive(graph1),
                         floydwarshall_imperative(graph1),
                         "Output incorrect")

    def test_floyd_2(self):
        """compare the recursive and imperative function with the second graph"""
        self.assertEqual(floydwarshall_recursive(graph2),
                         floydwarshall_imperative(graph2),
                         "Output incorrect")
 
    def test_floyd_3(self):
        """compare the recursive and imperative function with the third graph"""
        self.assertEqual(floydwarshall_recursive(graph3),
                         floydwarshall_imperative(graph3),
                         "Output incorrect")
        
    def test_floyd_4(self):
        """compare the recursive and imperative function with the fourth graph"""
        self.assertEqual(floydwarshall_recursive(graph4),
                         floydwarshall_imperative(graph4),
                         "Output incorrect")

if __name__ == '__main__':
    unittest.main()
