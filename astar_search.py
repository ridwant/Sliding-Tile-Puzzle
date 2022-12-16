import numpy as np
import time
from sortedcontainers import SortedList

def astar(start, goal, heuristic_fn, tmax=120):
    "Use the cost function to calculate the total cost h(n) = f(n) + g(n)"
    cost_fn = lambda q: q[0] + q[1]
    Q = SortedList([(0, heuristic_fn(start, goal), [start])], key=cost_fn)

    "Using set to remove duplicates states"
    visited = set()
    stime = time.time()
    while((time.time() - stime) < tmax):
        if len(Q) == 0:
          break
        N = Q.pop(0)
        distN, hN, statesN = N
        
        if statesN[-1] == goal:
            return {
                'succeeded': True,
                'path': statesN,
                'time': time.time() - stime,
            }

        if statesN[-1] in visited:
            continue
        else:
            visited.add(statesN[-1])
        
        vertices = statesN[-1].get_neighbours()
        for vertex in vertices:
            if vertex not in visited:
                Q.add((distN + 1, heuristic_fn(vertex, goal), statesN + [vertex]))
        
    return {
        'succeeded': False,
        'path': statesN,
        'time': time.time() - stime,
    }