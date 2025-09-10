# ===============================
# 8-Puzzle Problem - IDS Version
# ===============================

start_state = [[2, 8, 1],
               [0, 4, 3],
               [7, 6, 5]]

goal_state = [[1, 2, 3],
              [8, 4, 0],
              [7, 6, 5]]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_names = ['Up', 'Down', 'Left', 'Right']

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def deepcopy(state):
    return [row[:] for row in state]

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def dls(current_state, goal_state, limit, path, visited):
    if current_state == goal_state:
        return path

    if limit <= 0:
        return None

    x, y = find_blank(current_state)

    for i, (dx, dy) in enumerate(directions):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(current_state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            state_key = state_to_tuple(new_state)
            if state_key not in visited:
                visited.add(state_key)
                result = dls(new_state, goal_state, limit - 1, path + [direction_names[i]], visited)
                if result is not None:
                    return result
                visited.remove(state_key)

    return None

def iterative_deepening(start_state, goal_state, max_depth):
    for depth in range(max_depth + 1):
        print(f"Trying depth limit: {depth}")
        visited = set()
        visited.add(state_to_tuple(start_state))
        result = dls(start_state, goal_state, depth, [], visited)
        if result:
            return result, depth
    return None, max_depth

# ======================
# Main Execution Block
# ======================
if __name__ == "__main__":
    max_depth = 30
    print("Starting IDS on 8-puzzle (up to depth limit =", max_depth, ")")
    solution, depth_reached = iterative_deepening(start_state, goal_state, max_depth)

    if solution:
        print("\nSolution Found using IDS!")
        print("Moves:", solution)
        print("Total Steps:", len(solution))
        print("Found at depth:", depth_reached)
    else:
        print(f"No solution found within depth limit = {max_depth}.")
