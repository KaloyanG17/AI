# Q1.3 - Maze Solver using Impooved Algorithm (A* Search)
# Imports
from collections import deque
import time
from heapq import heappush, heappop
# Import the read_maze_file function from Q1_2.py
from Q1_2 import read_maze_file

# Change the maze file name here to test other mazes
mazeFile = "maze-Medium.txt"

# Solve the maze using A* Search
def solveMaze(maze):
    # Row and column lengths
    R, C = len(maze), len(maze[0])

    # Find the start position
    start = (0,0)
    for c in range(C):
        if maze[0][c] == '-':
            start = (0,c)
            break
    else:
        raise ValueError("No start position found")

    # Find the goal position
    goal = (R-1, 0)
    for c in range(C):
        if maze[R-1][c] == '-':
            goal = (R-1, c)
            break
    else:
        raise ValueError("No goal position found")

    # Define the heuristic function (Manhattan distance)
    def h(coord):
        return abs(coord[0]-goal[0]) + abs(coord[1]-goal[1])

    # Create the priority queue and append the start location
    queue = [(h(start), start, 0)]
    # Set directions you can move in
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    # Keep track of visited locations
    visited = [[False] * C for _ in range(R)]
    # Keep track of the previous location for getting the solution path
    came_from = {}
    # Keep track of the number of nodes explored
    numNodesExplored = 0
    # Start the timer
    startTime = time.time()

    # Start the search 
    while len(queue) != 0:
        # Get the next coordinate
        _, coord, cost = heappop(queue)
        # Mark the point as visited
        visited[coord[0]][coord[1]] = True
        # Increment the number of nodes explored
        numNodesExplored += 1
        
        # Check if we have reached the end
        if coord == goal:
            # Stop the timer
            endTime = time.time()
            # Calculate the number of steps in the path
            numSteps = cost
            # Return the number of nodes explored, the time taken, the number of steps in the path and the solution path
            path = []
            curr = goal
            while curr != start:
                path.append(curr)
                curr = came_from[curr]
            path.append(start)
            path.reverse()
            # Return the results
            return (numNodesExplored, endTime - startTime, numSteps, path)

        # Check all the directions you can move in 
        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            # Check if the new row and column are in bounds and if the point has been visited or is a wall 
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]):
                continue
            # Add the new point to the priority queue with the cost of the path so far plus the heuristic 
            heappush(queue, (cost + h((nr, nc)), (nr, nc), cost+1))
            # Add the new point to the came_from dictionary
            came_from[(nr, nc)] = coord

    # Stop the timer
    endTime = time.time()
    # No solution found so return -1 for the number of steps
    return (numNodesExplored, endTime - startTime, -1, path)


if __name__ == "__main__":
    # Read the maze from the file
    maze = read_maze_file(mazeFile)
    # Solve the maze
    numNodesExplored, timeTaken, numSteps, path = solveMaze(maze)
    # Check if no solution was found
    if numSteps == -1:
        print("No solution found")
    # Print the results
    print("Path: ")
    for p in path:
        print("(",p[0],",",p[1],")", end=" -> ")
    print("END")
    print("Number of nodes explored: ", numNodesExplored)
    print("Time taken: ", timeTaken , " seconds")
    print("Number of steps in the path: ", numSteps)
        
    