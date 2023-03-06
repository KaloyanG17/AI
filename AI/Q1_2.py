# Q1.2 - Maze Solver using Deep First Search Algorithm
# Imports
import time
from collections import deque

# Change the maze file name here to test other mazes
mazeFile = "maze-VLarge.txt"

# Solve the maze using DFS
def solveMaze(maze):
    # Row and column lengths of the maze
    R,C = len(maze), len(maze[0])

    # Find the start postion of the maze (the first '-' in the first row)
    start = (0,0)
    for c in range(C):
        if maze[0][c] == '-':
            start = (0,c)
            break
    else:
        # No start position found on the first row of the maze 
        raise ValueError("No start position found")

    # Create the stack and append the start location
    stack = [(start[0], start[1], 0)]
    # Set the directions you can move in (up, down, left, right) 
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    # Keep track of visited locations
    visited = [[False] * C for _ in range(R)]
    # Keep track of the previous location for getting the solution path
    prev = [[None] * C for _ in range(R)]
    # Keep track of the number of nodes explored
    numNodesExplored = 0
    # Start the timer
    startTime = time.time()

    # Start the search 
    while len(stack) != 0:
        # Get the next coordinate
        coord = stack.pop()
        # Mark the point as visited
        visited[coord[0]][coord[1]] = True
        # Increment the number of nodes explored
        numNodesExplored += 1

        # Check if we have reached the end of the maze (the last '-' in the last row)
        if coord[0] == R-1 and maze[coord[0]][coord[1]] == "-":
            # Stop the timer
            endTime = time.time()
            #Calculate the number of steps in the solution path
            numSteps = coord[2]
            # Get the solution path by backtracking from the end to the start 
            path = [coord]
            while prev[path[-1][0]][path[-1][1]] is not None:
                path.append(prev[path[-1][0]][path[-1][1]])
            path.reverse()
            # Return the results 
            return (numNodesExplored, endTime - startTime, numSteps, path)

        # Check all the directions you can move in 
        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            # Check if the new point is valid (not out of bounds, not a wall, not visited) 
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]):
                continue
            # Add the new point to the stack 
            stack.append((nr, nc, coord[2]+1))
            # Set the previous location of the new point
            prev[nr][nc] = coord

    # Stop the timer
    endTime = time.time()
    # No solution found so return -1 for the number of steps and None for the path
    return (numNodesExplored, endTime - startTime, -1 , None)


# Read the maze from the file (also used in Q1.3 through import)
def read_maze_file(filename):
    # Set a list to store the maze
    maze = []
    # Open the file and read the maze
    with open(filename) as f:
        # Read each line in the file
        for line in f:
            # If line is empty remove it
            if not line.strip():
                continue
            # Remove the newline character and replace spaces with nothing
            line = line.strip()
            line = line.replace(" ", "")
            # Add the line to the maze
            maze.append([i for i in line])
    # Return the maze
    return maze

# Main function
if __name__ == "__main__":
    # Read the maze from the file 
    maze = read_maze_file(mazeFile)
    # Solve the maze
    numNodesExplored, timeTaken, numSteps, path = solveMaze(maze)
    # Check if a solution was found
    if numSteps == -1:
        print("No solution found")
    
    # Print the results
    # print("Path: ")
    # for p in path:
    #     print("(",p[0],",",p[1],")", end=" -> ")
    # print("END")
    print("Number of nodes explored: ", numNodesExplored)
    print("Time taken: ", timeTaken , " seconds")
    print("Number of steps in the path: ", numSteps)

        



