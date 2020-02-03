from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.adjacent = {}
        file = open( filename, 'r' )
        for line in file:
            pair = line.split()
            if pair[0] in self.adjacent:
                self.adjacent[pair[0]]+= [pair[1]]
            else:
                self.adjacent[pair[0]] = [pair[1]]
            if pair[1] in self.adjacent:
                self.adjacent[pair[1]]+= [pair[0]]
            else:
                self.adjacent[pair[1]] = [pair[0]]
        file.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.adjacent:
            self.adjacent[key] = []

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.adjacent:
            return key
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.adjacent[v1] += [v2]
        self.adjacent[v2] += [v1]

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        keys = list(self.adjacent.keys())
        keys.sort()
        return keys

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        visited = []
        thelist = []
        for item in self.get_vertices():
            if item not in visited:
                set = self.dfs_help( self.adjacent, item )
                visited += set
                if set != []:
                    set.sort()
                    thelist += [set]
        return thelist

    def dfs_help(self, graph, vertex):
        stack = Stack( len(self.adjacent) )
        stack.push( vertex )
        visited = []
        visited += [vertex]
        while not stack.is_empty():
            vis = stack.pop()
            hi= graph[vis]
            if hi !=[]:
                hi.sort()
                for child in hi:
                    if child not in visited:
                        stack.push( child )
                        visited += [child]
        return visited

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''

        sets = self.conn_components()
        for set in sets:
            colorlist = self.bfs_color( set )
            for vert in set:
                for child in self.adjacent[vert]:
                    if colorlist[child] % 2 == colorlist[vert] % 2:
                        return False
        return True


    def bfs_color(self, cluster):
        queue = Queue( len( cluster ) )
        queue.enqueue( cluster[0] )
        visited = {cluster[0]: 0}
        while not queue.is_empty():
            next = queue.dequeue()
            color = visited[next] + 1
            for child in self.adjacent[next]:
                if child not in visited:
                    queue.enqueue( child )
                    visited[child] = color
        return visited