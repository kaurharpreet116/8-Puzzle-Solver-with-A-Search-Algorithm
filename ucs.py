import heapq

# ===============================
# 8-Puzzle Problem - UCS Version
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

def ucs(start_state, goal_state):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_state, []))  # (cost, state, path)
    visited = set()

    while priority_queue:
        cost, current_state, path = heapq.heappop(priority_queue)
        state_key = state_to_tuple(current_state)

        if state_key in visited:
            continue
        visited.add(state_key)

        if current_state == goal_state:
            return path, cost

        x, y = find_blank(current_state)

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = deepcopy(current_state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_key = state_to_tuple(new_state)

                if new_key not in visited:
                    heapq.heappush(priority_queue, (cost + 1, new_state, path + [direction_names[i]]))

    return None, -1

# ======================
# Main Execution Block
# ======================
if __name__ == "__main__":
    print("Starting UCS on 8-puzzle...")
    solution, total_cost = ucs(start_state, goal_state)

    if solution:
        print("Solution Found using UCS!")
        print("Moves:", solution)
        print("Total Steps:", len(solution))
        print("Total Cost:", total_cost)
    else:
        print("No solution found using UCS.")
