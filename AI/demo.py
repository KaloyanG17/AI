import time 
from collections import deque 

 
def readmazefile(filename): 
    # Initialize the maze as an empty list
    maze = [] 
    # Read the maze file and return a 2D list 
    with open(filename) as f: 
        for line in f:
            if not line.strip(): 
                continue
            # Remove the spaces and newlines from the line    
            line = line.strip()
            line = line.replace(" ", "")
            # Add the line to the maze
            maze.append(list(line))
    # Return the maze
    return maze 

# Read the maze file 
maze = readmazefile("maze-Small.txt") 
#print(maze) 

def get_start(maze):
    """Returns the start cell in a maze"""
    start = (0,0)
    for col in range(len(maze[0])):
        if maze[0][col] == '-':
            return (0,col)
    

def get_neighbours(maze, node):
    """Returns the unvisited neighbours of a node"""
    neighbours = []
    # Check if the node is not the last row
    if node[0] != len(maze) - 1:
        # Check if the node below is not a wall
        if maze[node[0] + 1][node[1]] != '#':
            # Add the node below to the neighbours list
            neighbours.append((node[0] + 1, node[1]))
    # Check if the node is not the first row
    if node[0] != 0:
        # Check if the node above is not a wall
        if maze[node[0] - 1][node[1]] != '#':
            # Add the node above to the neighbours list
            neighbours.append((node[0] - 1, node[1]))
    # Check if the node is not the last column
    if node[1] != len(maze[0]) - 1:
        # Check if the node to the right is not a wall
        if maze[node[0]][node[1] + 1] != '#':
            # Add the node to the right to the neighbours list
            neighbours.append((node[0], node[1] + 1))
    # Check if the node is not the first column
    if node[1] != 0:
        # Check if the node to the left is not a wall
        if maze[node[0]][node[1] - 1] != '#':
            # Add the node to the left to the neighbours list
            neighbours.append((node[0], node[1] - 1))
    return neighbours


def dfs(maze, start, end):
    """Solves a maze using depth-first search"""
    # Initialize the stack with the start node
    stack = [[start[0], start[1]]]
    # Initialize the parent dictionary
    parent = {start: None}
    # Initialize the number of nodes explored to 0
    nodes_explored = 0
    # Initialize the number of steps to 0
    num_steps = 0

    # mark visited
    maze[start[0]][start[1]] = 'V'

    # Start the timer
    start_time = time.time()

    # Loop until the stack is empty
    while len(stack) != 0:
        # Increment the number of steps
        num_steps += 1

        # Pop a node from the stack
        current_node = stack.pop()

        # Check if the current node is the end node
        if current_node == end:
            # Stop the timer
            end_time = time.time()
            # Calculate the execution time
            execution_time = end_time - start_time
            #Calculate the number of steps in the solution path
            num_steps = current_node[0] + current_node[1] - 1
            # Return the path, nodes explored, execution time, and number of steps
            return maze, nodes_explored, execution_time, num_steps

        # Get the neighbours of the current node
        neighbours = get_neighbours(maze, current_node)
        # Loop through the neighbours
        for neighbour in neighbours:
            # Check if the neighbour is not in the parent dictionary
            if neighbour not in parent:
                # Increment the number of nodes explored
                nodes_explored += 1
                # Add the neighbour to the parent dictionary
                parent[neighbour] = current_node
                # Add the neighbour to the stack
                stack.append(neighbour)
                # Mark the neighbour as visited
                maze[neighbour[0]][neighbour[1]] = 'V'

    # Stop the timer
    end_time = time.time()
    # Calculate the execution time
    execution_time = end_time - start_time
    # Return None, nodes explored, execution time, and number of steps
    return None, nodes_explored, execution_time, num_steps

# Find the start and cells
start = get_start(maze)
end = (len(maze)-1, maze[len(maze)-1].index('-'))

# Print the path and performance statistics
path, nodes_explored, execution_time, num_steps = dfs(maze, start, end)
if path is not None:
    print(f"Path found! Number of steps: {num_steps}")
    print(f"Nodes explored: {nodes_explored}")
    print(f"Execution time: {execution_time} seconds")
else:
    print("No path found")