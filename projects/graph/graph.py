"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            print("This vertex already exists!")
    def add_edge(self, start_vertex, end_vertex):
        """
        Add a directed edge to the graph.
        """
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex].add(end_vertex)
        elif start_vertex not in self.vertices:
            print(f"The following vertex does not exist: {start_vertex}")
        elif end_vertex not in self.vertices:
            print(f"The following vertex does not exist: {end_vertex}")
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for next_vert in self.vertices[v]:
                    s.push(next_vert)
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Add current vertex to visited
        visited.add(starting_vertex)

        # Then add all of its unvisited children to the call stack
        for child in self.vertices[starting_vertex]:
            if child not in visited:
                self.dft_recursive(child,visited)
        
        return visited
                
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Store found vertices
        found = []
        # While the queue is not empty...
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            # If the vertex has not been found
            if vertex not in found:
                if vertex is destination_vertex:
                    return path
                found.append(vertex)
                # For each child vertex, add it to the queue of possible paths
                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    q.enqueue(new_path)
                
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # Store found vertices
        found = []
        # While the queue is not empty...
        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]
            # If the vertex has not been found
            if vertex not in found:
                if vertex is destination_vertex:
                    return path
                found.append(vertex)
                # For each child vertex, add it to the stack of possible paths
                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    s.push(new_path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
