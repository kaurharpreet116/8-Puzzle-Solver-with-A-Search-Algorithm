# 🧠 8-Puzzle Solver Using A* Search Algorithm

## 📌 Project Overview

This project implements an AI-based solution to the classic **8-Puzzle Problem** using various search algorithms, with a focus on the **A\*** algorithm for optimal performance.

The 8-puzzle is a 3x3 sliding puzzle consisting of 8 numbered tiles and one blank space. The objective is to reach a specific goal configuration by sliding tiles into the blank space.

---

## 🎯 Objective

- Solve the 8-puzzle efficiently using A* search
- Compare A* with other search strategies (BFS, DFS, UCS, IDS, GBFS, etc.)
- Evaluate each algorithm based on:
  - Total moves to goal
  - Execution time
  - Memory efficiency
  - Optimality

---

## 🧮 Algorithms Implemented

| Algorithm        | Heuristic Used     | Optimal | Complete |
|------------------|--------------------|---------|----------|
| BFS              | None               | ✅      | ✅        |
| DFS              | None               | ❌      | ❌        |
| DLS              | None               | ❌      | ❌        |
| IDS              | None               | ✅      | ✅        |
| UCS              | Cost-only (g(n))   | ✅      | ✅        |
| Greedy Best-First| Heuristic only (h) | ❌      | ❌        |
| **A\***         | **g(n) + h(n)**     | ✅      | ✅        |

---

## 🚀 A* Search Overview

A* uses the formula:  
```f(n) = g(n) + h(n)```  
Where:
- `g(n)` = cost from the start node
- `h(n)` = estimated cost to the goal using **Manhattan Distance**

Heuristic ensures efficient, optimal pathfinding.

---

## 🛠️ Project Structure

```bash
8PuzzleSolver/
├── HarpreetKaur_FinalProject.ipynb   # Main Colab notebook with all code
├── README.md                         # Project documentation
├── example_output.png                # Sample solution visualization (optional)
├── requirements.txt                  # Dependencies (if applicable)
└── ppt/                              # PowerPoint presentation (if available)
```

---

## 📦 Requirements

- Python 3.8+
- Jupyter Notebook / Google Colab
- Libraries:
  - `heapq`
  - `copy`
  - `time`
  - `collections`

> *No external packages needed — fully standard Python.*

---

## ▶️ How to Run

1. Open `HarpreetKaur_FinalProject.ipynb` in **Google Colab** or Jupyter.
2. Set `start_state` and `goal_state`.
3. Run the `a_star(start, goal)` function.
4. The path, number of steps, and performance metrics will be printed.

---

## ✅ Sample Output

```bash
Initial State:
2 8 1
0 4 3
7 6 5

Goal State:
1 2 3
8 0 4
7 6 5

Solution Path: ['Right', 'Up', 'Left', 'Down', ...]
Total Moves: 9
Time Taken: 0.02s
```

---

## 📊 Performance Comparison

A* consistently outperforms other methods by:
- Reducing number of explored nodes
- Providing shortest path
- Scaling well to harder puzzles (e.g., 15-puzzle)

---

## 🧠 Real-World Applications

- Game AI and puzzle solvers
- Pathfinding in maps and navigation
- Robotics planning and motion control
- Logistics route optimization

---

## 👩‍💻 Author

**Harpreet Kaur**  
Artificial Intelligence – Final Project  
June 17, 2025

---

## 📚 References

- Russell & Norvig. *Artificial Intelligence: A Modern Approach*
- GeeksForGeeks: [A* Algorithm](https://www.geeksforgeeks.org/a-search-algorithm/)
- Wikipedia: [8-Puzzle Problem](https://en.wikipedia.org/wiki/15_puzzle)