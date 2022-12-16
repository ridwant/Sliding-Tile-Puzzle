import numpy as np
import time

def dfs(start, goal, tmax=120):
    Q = [[start]]
    visited = set([start])
    stime = time.time()
    while((time.time() - stime) < tmax):
        if len(Q) == 0:
            break
        N = Q.pop()
        if N[-1] == goal:
            return {
                'succeeded': True,
                'path': N,
                'time': time.time() - stime,
            }
        
        vertices = N[-1].get_neighbours()
        for vertex in vertices: 
            if vertex not in visited:
                visited.add(vertex)
                Q.append(N + [vertex])
    return {
        'succeeded': False,
        'path': N,
        'time': time.time() - stime,
    }