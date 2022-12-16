import argparse
import time

from SlidingPuzzleMain import (
    SlidingPuzzle
)

from breadth_first_search import (
    bfs
)
from depth_first_search import (
    dfs
)

from astar_search import (
    astar
)

from heuristics import (
    zero_heuristic,
    misplaced_tiles_heuristic,
    manhattan_heuristic,
    linear_conflicts_heuristic
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problemFile", type=str, default=None)
    parser.add_argument("methodName", type=str, default=None)
    parser.add_argument("tmax", type=int, default=None)
    parser.add_argument("solutionFile", type=str, default=None)
    args = parser.parse_args()
    
    problemFile = args.problemFile
    methodName = args.methodName
    tmax = args.tmax
    solutionFile = args.solutionFile
    
    file = open(problemFile, "r")
    N, M = file.readline().split()
    file.readline()
    initial_state = []
    goal_state = []
    for line in file:
        if line.strip() == '':
            break
        initial_state+=line.split()

    for line in file:
        if line.strip() == '':
            break
        goal_state+=line.split()

    initial_state = [int(i) for i in initial_state]
    goal_state = [int(i) for i in goal_state]
    start = SlidingPuzzle(int(N),int(M), initial_state)
    goal = SlidingPuzzle(int(N),int(M), goal_state)
    start_time = time.time()

    if methodName.lower().strip() == 'bfs':
        solution = bfs(start, goal, tmax)
    if methodName.lower().strip() == 'dfs':
        solution = dfs(start, goal, tmax)
    if methodName.lower().strip() == 'astarh0':
        solution = astar(start, goal, zero_heuristic, tmax)
    if methodName.lower().strip() == 'astarh1':
        solution = astar(start, goal, misplaced_tiles_heuristic, tmax)
    if methodName.lower().strip() == 'astarh2':
        solution = astar(start, goal, manhattan_heuristic, tmax)
    if methodName.lower().strip() == 'astarh3':
        solution = astar(start, goal, linear_conflicts_heuristic, tmax)
    end_time = time.time()
    
    output = open(solutionFile, "w+")
    for path in solution['path']:
      line = path.get_zero_index_position()
      output.write(str(line[0]) + " " +str(line[1]) + "\n")
    
    output.close()
    file.close()

if __name__ == "__main__":
    main()
