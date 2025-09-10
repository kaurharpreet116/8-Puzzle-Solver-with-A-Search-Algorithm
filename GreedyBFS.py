import heapq

# ==================================
# 8-Puzzle Problem - A* Search
# ==================================

start_state = [[2, 8, 1],
               [0, 4, 3],
               [7, 6, 5]]

goal_state = [[1, 2, 3],
              [8, 0, 4],
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

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            distance += abs(x - i) + abs(y - j)
    return distance

def a_star(start, goal):
    pq = []
    visited = set()
    g_costs = {state_to_tuple(start): 0}

    heapq.heappush(pq, (manhattan_distance(start, goal), 0, start, []))  # (f = g + h, g, state, path)

    while pq:
        f, g, current_state, path = heapq.heappop(pq)
        state_key = state_to_tuple(current_state)

        if state_key in visited:
            continue
        visited.add(state_key)

        if current_state == goal:
            return path

        x, y = find_blank(current_state)

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = deepcopy(current_state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_key = state_to_tuple(new_state)
                new_g = g + 1
                new_f = new_g + manhattan_distance(new_state, goal)

                if new_key not in visited and (new_key not in g_costs or new_g < g_costs[new_key]):
                    g_costs[new_key] = new_g
                    heapq.heappush(pq, (new_f, new_g, new_state, path + [direction_names[i]]))

    return None

# ======================
# Main Execution Block
# ======================
if __name__ == "__main__":
    print("Starting A* Search on 8-Puzzle...\n")
    solution = a_star(start_state, goal_state)

    if solution:
        print("✅ Solution Found using A*!")
        print("Moves:", solution)
        print("Total Steps:", len(solution))
    else:
        print("❌ No solution found.")
