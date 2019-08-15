# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west. For example:
from util import Queue

islands = [[0, 1, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 0, 0]]

class IslandFinder:
    def __init__(self,island_matrix):
        self.island_matrix = island_matrix
        self.parcel_graph = {}
        self.islands_found = 0
        self.generate_graph()
        self.num_islands()

    def generate_graph(self):
        for row in range(len(self.island_matrix)):
            for col in range(len(self.island_matrix[0])):
                if self.island_matrix[row][col] == 1 and (row,col) not in self.parcel_graph:
                    q = Queue()
                    q.enqueue((row, col))
                    self.islands_found += 1
                    print(f"\n \U0001F3D6\U0001F3D6\U0001F3D6 A new island was found! #{self.islands_found} \U0001F3D6\U0001F3D6\U0001F3D6")
        
                    while q.size() >= 1:
                        current_parcel = q.dequeue()
                        current_row = current_parcel[0]
                        current_col = current_parcel[1]
                        self.parcel_graph[current_parcel] = self.islands_found
        
                        # North
                        if current_row-1 >= 0 and self.island_matrix[current_row-1][current_col] == 1 and (current_row-1,current_col) not in self.parcel_graph:
                            print(f"-- North of {current_parcel}, a connecting island parcel was found: {(current_row-1,current_col)}")
                            q.enqueue((current_row-1,current_col))
                        # South
                        if current_row+1 < len(self.island_matrix) and self.island_matrix[current_row+1][current_col] == 1  and (current_row+1,current_col) not in self.parcel_graph:
                            print(f"-- South of {current_parcel}, a connecting island parcel was found: {(current_row+1,current_col)}")
                            q.enqueue((current_row+1,current_col))
                        # West
                        if current_col-1 >= 0 and self.island_matrix[current_row][current_col-1] == 1 and (current_row,current_col-1) not in self.parcel_graph:
                            print(f"-- West of {current_parcel}, a connecting island parcel was found: {(current_row,current_col-1)}")
                            q.enqueue((current_row,current_col-1))
                        # East
                        if current_col+1 < len(self.island_matrix[0]) and self.island_matrix[current_row][current_col+1] == 1 and (current_row,current_col+1) not in self.parcel_graph:
                            print(f"-- East of {current_parcel}, a connecting island parcel was found: {(current_row,current_col+1)}")
                            q.enqueue((current_row,current_col+1))
    
    def num_islands(self):
        #print(f"Parcel Graph: {self.parcel_graph}")
        print(f"\n \U00002600\U00002600\U00002600 Islands Found: {self.islands_found} \U00002600\U00002600\U00002600")
        return self.islands_found

IslandFinder(islands)