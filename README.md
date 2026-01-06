 # Pathfinding Visualizer (A* Algorithm) 🚀

A full-stack web application that visualizes the A* pathfinding algorithm in real-time. 
Originally a Python console script, this project has been upgraded to a Flask web app with an interactive Cyberpunk UI.

## 🌟 Features
* **Interactive Grid:** Draw walls, set start/end points.
* **Weighted Nodes:** Add "Terrain" costs (Mud, Water, etc.) that the algorithm must account for.
* **Real-time Visualization:** Watch the algorithm scan and find the shortest path.
* **Full-Stack:** Python (Flask) backend + HTML/CSS/JS frontend.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3 (Cyberpunk Theme), JavaScript (Fetch API)
* **Algorithm:** A* Search (Manhattan/Euclidean Heuristic)

## 🚀 How to Run Locally
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install flask flask-cors
    ```
3.  Start the backend server:
    ```bash
    python app.py
    ```
4.  Open your browser and navigate to: `http://localhost:5001`