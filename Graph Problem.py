import csv

class System:
    steps = [   
        [-1,0], # Top Step
        [0,1],  # Right Step
        [1,0], # Bottom Step
        [0,-1] # Left Step
    ]
    
    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city = list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows = len(self.star_city)
        self.star_city_cols = len(self.star_city[0])

    def check_limits(self, row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self, row, col):
        neighbours = []
        #loop through top, right, bottom and left adjacent nodes to get the neighbor
        # only if the altitude of adjacent node is lower or equal to the current node 
        # and is not already present in neighbors list
        for i in System.steps:
            if self.check_limits(row+i[0], col+i[1]):
                if self.star_city[row+i[0]][col+i[1]] <= self.star_city[row][col] and (row+i[0], col+i[1]) not in neighbours:
                    neighbours.append((row+i[0], col+i[1]))
        return neighbours

    def find_route(self,source,destination):
        #empty que and visited lists
        visited = []
        que = []

        #add 1st node in visited and que lists
        visited.append(source)
        que.append(visited)


        #traverse all the nodes from que till the que is not empty
        # or destination is not found
        while que:
            #get the first path from que and mark it visited
            visited = que.pop(0)
            #get the last node from the visited path
            last = visited[len(visited)-1]
            #if the last node from visited path is destination then return the visited path
            if last == destination:
                return visited
            #get each neighbours of the last node one by one
            for neighbour in self.get_neighbours(last[0], last[1]):
                #if neighbour is not visited then make a new path with the existing nodes from visited list and the neighbour
                # and add the new path in que
                if neighbour not in visited:
                    new_path = visited.copy()
                    new_path.append(neighbour)
                    que.append(new_path) 
        #return empty list if path not found
        return []


    def Bluevalley_to_Smallville_route(self):
        # Helper function to perform DFS from Blue Valley to Smallville
        def dfs(curr_row, curr_col, path):
            if curr_row < 0 or curr_row >= len(self.matrix) or curr_col < 0 or curr_col >= len(self.matrix[0]):
                # Out of bounds, return False
                return False

            if [curr_row, curr_col] in path:
                # Already visited, return False
                return False

            # Check if the current cell is in Smallville (rightmost column)
            if curr_col == len(self.matrix[0]) - 1:
                # Add the current cell to the path
                path.append([curr_row, curr_col])
                return True

            # Check if altitude of current cell is higher than or equal to the right neighbor
            if self.matrix[curr_row][curr_col] > self.matrix[curr_row][curr_col + 1]:
                return False

            # Add the current cell to the path
            path.append([curr_row, curr_col])

            # Recursively explore neighboring cells
            if dfs(curr_row - 1, curr_col, path) or dfs(curr_row, curr_col + 1, path) \
                    or dfs(curr_row + 1, curr_col, path) or dfs(curr_row, curr_col - 1, path):
                return True

            # If no path found, backtrack and remove the current cell from the path
            path.pop()
            return False

        # Initialize an empty path and call the DFS function starting from each cell in Blue Valley
        path = []
        for row in range(len(self.matrix)):
            if dfs(row, 0, path):
                break

        # Return the resulting path as a 2D list of grid coordinates
        return path        #row number and column number of Source city i.e., Bluevalley

        #row number and column number of Destination city i.e., Smallville
        
        #flag indicating route not found initially

                #if route is non empty so display the route and mark the flag as found and break.

            #if flag set to found, stop finding further routes

        pass
        
if __name__ == "__main__":
    test_system1 = System()
    
    #Getting data in 2D matrix
    test_system1.config_system('city_data.csv')
    
    #Finding path between Source node to Destination node
    route = test_system1.find_route((3,0),(4,2))
    print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
    for nodenum, node in enumerate(route):
        if nodenum != len(route)-1:
            print(f"({node[0]}, {node[1]}) ---->", end=" ")
        else:
            print(f"({node[0]}, {node[1]})", end=" ")
    
    #Finding path between Bluevalley to Smallville   
    test_system1.Bluevalley_to_Smallville_route()
