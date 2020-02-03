import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_addv(self):
        g = Graph( 'test2.txt' )
        g.add_vertex('v10')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v10'], ['v4', 'v6', 'v7', 'v8']])
        self.assertEqual(g.get_vertex('v1'), 'v1')
        self.assertEqual( g.get_vertex( 'v00' ), None )
        self.assertEqual( g.add_edge('v8', 'v10' ), None )
        self.assertEqual(g.get_vertices(), ['v1','v10', 'v2', 'v3', 'v4', 'v6', 'v7', 'v8'])


if __name__ == '__main__':
   unittest.main()
