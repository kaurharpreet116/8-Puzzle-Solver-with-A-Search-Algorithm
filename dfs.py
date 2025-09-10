def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == goal_state

def deepcopy(state):
    return [row[:] for row in state]

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def dfs(start):
    stack = [(start, [], set())]  # stack holds (state, path, visited)
    step = 0

    while stack:
        current_state, path, visited = stack.pop()
        visited.add(state_to_tuple(current_state))

        if is_goal(current_state):
            print("Goal reached in", len(path), "steps!")
            return path

        x, y = find_blank(current_state)
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = deepcopy(current_state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_tuple = state_to_tuple(new_state)
                if new_tuple not in visited:
                    stack.append((new_state, path + [direction_names[i]], visited.copy()))
        
        step += 1
        if step % 1000 == 0:
            print("Explored", step, "states...")

    print("No solution found.")
    return None

# ======================
# Main Execution Block
# ======================
if __name__ == "__main__":
    # Define the puzzle
    start_state = [[2, 8, 1],
                   [0, 4, 3],
                   [7, 6, 5]]

    goal_state = [[1, 2, 3],
                  [8, 4, 0],
                  [7, 6, 5]]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    direction_names = ['Up', 'Down', 'Left', 'Right']

    print("Starting DFS on 8-puzzle...")
    solution = dfs(start_state)

    if solution:
        print("Solution Path:")
        for move in solution:
            print(move)
        print("Total Moves:", len(solution))
    else:
        print("No solution found.")
