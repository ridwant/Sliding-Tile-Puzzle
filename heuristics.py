import numpy as np


def get_key(val, ditc):
    for key, value in ditc.items():
        if val == value:
            return key

    return -1


def count_conf(value, start, goal):
    count = 0
    for ii in start:
        for jj in goal:
            if ii == jj and ii != value and ii != 0:
                count += 1
    return count


def check_conflicts(start_row, goal_row, weight):
    conflict_array = {}
    for ii, srow in enumerate(start_row):
        for jj, grow in enumerate(goal_row):
            if srow == grow and srow != 0 and ii + 1 < len(start_row):
                conflict = count_conf(srow, start_row[ii + 1 :], goal_row[:jj])
                conflict_array[ii] = conflict
    if conflict_array:
        max_conflict = max(conflict_array.values())
    else:
        max_conflict = 0
    if max_conflict == 0:
        return weight * 2
    else:
        conf_index = get_key(max_conflict, conflict_array)
        new_start = start_row.copy()
        new_start[conf_index] = -2
        weight += 1
        return check_conflicts(new_start, goal_row, weight)


def zero_heuristic(start, goal):
    return 0


def misplaced_tiles_heuristic(start, goal):
    i = 0
    count = 0
    for i in range(len(start.state)):
        if start.state[i] != goal.state[i]:
            count += 1
        i += 1
    return count


def manhattan_heuristic(start, goal):
    all_unique_vals = list(set(start.state))
    if all_unique_vals[len(all_unique_vals) - 1] == -1:
        all_unique_vals.remove(-1)
    s = np.reshape(start.state, (start.nrows, start.ncols))
    g = np.reshape(goal.state, (goal.nrows, goal.ncols))
    dist = 0
    for ii in all_unique_vals:
        x = np.argwhere(s == ii)
        y = np.argwhere(g == ii)
        distances = []
        for x1, y1 in x:
            calc_dist = start.nrows * start.ncols
            for x2, y2 in y:
                calc_dist = min(abs(x1 - x2) + abs(y1 - y2), calc_dist)
            distances.append(calc_dist)
        dist += sum(distances)
    return dist


def linear_conflicts_heuristic(start, goal):
    manhattan = manhattan_heuristic(start, goal)
    s = np.reshape(start.state, (start.nrows, start.ncols))
    g = np.reshape(goal.state, (goal.nrows, goal.ncols))
    srows = [row for row in s]
    grows = [row for row in g]
    s_tp = np.transpose(s)
    g_tp = np.transpose(g)
    scols = [col for col in s_tp]
    gcols = [col for col in g_tp]
    conflict_weight = 0
    for index, row in enumerate(srows):
        conflict_weight += check_conflicts(row, grows[index], 0)
    for index, col in enumerate(scols):
        conflict_weight += check_conflicts(col, gcols[index], 0)

    return manhattan + conflict_weight
