# 8-Puzzle-Solver-with-A-Search-Algorithm
A Python implementation of the classic 8-Puzzle problem using search algorithms, with a focus on the A* algorithm. Demonstrates optimal pathfinding, heuristic evaluation, and comparison with BFS, DFS, UCS, and Greedy approaches.
# 8-Puzzle Solver with A* Search

## 📌 Overview
This project implements the **8-Puzzle problem solver** using multiple search algorithms, with a focus on the **A\*** algorithm.  
The puzzle consists of a 3x3 grid with 8 numbered tiles and one empty space, and the goal is to reach the desired configuration with the fewest moves.

## 🚀 Why A*?
The A* algorithm combines the cost so far (`g(n)`) with a heuristic estimate (`h(n)`) to find the most efficient path: f(n) = g(n) + h(n)

This ensures both **optimality** and **efficiency**, making A* more effective than BFS, DFS, UCS, or Greedy.

## 🛠️ Features
- Solve the 8-puzzle using **A\*** and compare with BFS, DFS, UCS, and Greedy.  
- Heuristics supported: **Misplaced Tiles** and **Manhattan Distance**.  
- Step-by-step puzzle-solving process.  
- Performance analysis of different algorithms.  

## ▶️ Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/8-Puzzle-Solver.git
   cd 8-Puzzle-Solver
2. Run the program: python main.py

📊 Results
A*: Finds optimal solutions efficiently.

BFS/UCS: Correct but memory-heavy.

DFS: Fast but not always reliable.

Greedy: Quick but non-optimal.
