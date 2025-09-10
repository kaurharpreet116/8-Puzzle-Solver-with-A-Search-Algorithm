from collections import deque

# Start and goal states from your image
start_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

goal_state = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

# Moves: (dx, dy) for Up, Down, Left, Right
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def move_blank(state, dx, dy):
    x, y = find_blank(state)
    nx, ny = x + dx, y + dy
    if 0 <= nx < 3 and 0 <= ny < 3:
        new_state = [list(row) for row in state]
        new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
        return to_tuple(new_state)
    return None

def bfs(start_state):
    start_state = to_tuple(start_state)
    if start_state == goal_state:
        return [start_state]

    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)

    while queue:
        current_state, path = queue.popleft()

        for dx, dy in MOVES:
            new_state = move_blank(current_state, dx, dy)
            if new_state and new_state not in visited:
                if new_state == goal_state:
                    return path + [current_state, new_state]
                queue.append((new_state, path + [current_state]))
                visited.add(new_state)
    return None

def print_state(state):
    for row in state:
        print(' '.join(str(num) if num != 0 else '□' for num in row))
    print()

# Run the BFS Solver
if __name__ == "__main__":
    print("Solving 8-Puzzle using BFS...\n")
    solution = bfs(start_state)

    if solution:
        print(f"✅ Puzzle solved in {len(solution)-1} moves!\n")
        for i, state in enumerate(solution):
            print(f"Step {i}:")
            print_state(state)
    else:
        print("❌ No solution found.")
