import heapq

def input_puzzle(prompt):
    print(f"\n{prompt}")
    puzzle = []
    for i in range(3):
        row = input(f"Enter Row {i+1} (space-separated, use 0 for blank): ").strip().split()
        puzzle.extend([int(n) for n in row])
    return tuple(puzzle)

def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        x1, y1 = divmod(state.index(num), 3)
        x2, y2 = divmod(goal.index(num), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            n_idx = nx*3 + ny
            new_state = list(state)
            new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in visited:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f, tentative_g, neighbor))

    return None

def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(str(n) if n != 0 else '□' for n in state[i:i+3]))
    print()

if __name__ == "__main__":
    print("=== 8 Puzzle Solver using A* Search ===")

    start = input_puzzle("Enter START state")
    goal = input_puzzle("Enter GOAL state")

    print("\nSolving...\n")
    path = a_star(start, goal)

    if path:
        print(f"✅ Puzzle solved in {len(path)-1} steps!\n")
        for i, state in enumerate(path):
            print(f"Step {i}:")
            print_state(state)
    else:
        print("❌ No solution found. Make sure the puzzle is solvable.")
1