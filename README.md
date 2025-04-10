# 🚀A-star-Algorithm-for-shortest-path-problems
 This project explores A* (A-star) algorithm and its application for solving the shortest path problems, which are core concepts of various fields like robotics, transportation, artificial intelligence, and computer games. The A* algorithm is a widely-used pathfinding algorithm that extends Dijkstra’s Algorithm by the integration of heuristic information to guide its search more efficiently. It evaluates paths by combining the cost to reach a node (g(n)) and a heuristic estimate of the cost to reach the goal from that node(h(n)), evaluating a total cost function f(n) = g(n) + h(n). This approach enables A* to find the most efficient path to the goal with reduced computation, assuming the heuristic is admissible and consistent.

 I used Euclidean distance as the heuristic to guide the search efficiently. The input is a 2D grid, where the start and end points are given as tuples. For each node, I ensured it was valid and generated all 8 possible neighboring nodes (including diagonals). The algorithm processes the grid and highlights the optimal path from the source to the destination. To visualize the result, I used Matplotlib—marking the start point in red, the destination in green, and the final path in blue—making it easy to understand how A* works in action.

 📍The project includes:

📌Main algorithm file that executes the A* logic.

📌Visualization module using Matplotlib, which generates an image of the grid showing the start point in red, the destination in green, and the optimal path in blue.

📌Five different grid matrix files that simulate various levels of complexity. Each grid represents a new challenge, gradually increasing the difficulty of pathfinding, and all of them call the main algorithm.

📌This setup offers a clear and interactive way to understand how A* works across different scenarios and complexities.

## 🛠 Installation

1. Ensure Python3 is installed:
   python3 --version
2. Install the required library:
   pip install matplotlib
   
▶️ Usage:

✅.  python3 Grid.py

✅.  python3 Grid10x10.py

✅.  python3 grid12x12.py

✅.  # ...up to GridCom.py

   
