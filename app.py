from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from A_star import a_star_search

# Initialize Flask with explicit folder names
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}})

# 1. SERVE THE HTML PAGE
@app.route("/")
def index():
    return render_template("index.html")

# 2. HANDLE THE ALGORITHM REQUEST
@app.route("/run-pathfinding", methods=["POST"])
def run():
    try:
        data = request.json
        
        # Extract data from the frontend
        grid = data["matrix"]
        start = tuple(data["start"])
        end = tuple(data["end"])

        # Force start/end to be walkable (just in case)
        grid[start[0]][start[1]] = 1
        grid[end[0]][end[1]] = 1

        # Run the A* Algorithm
        visited, path = a_star_search(grid, start, end)

        # Return results to frontend
        return jsonify({
            "visited": visited,
            "path": path
        })

    except Exception as e:
        print("BACKEND ERROR:", e)
        return jsonify({"error": str(e)}), 500

# 3. START THE SERVER (Local Testing Only)
# This block is ignored by Render (which uses Gunicorn), but vital for local testing.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

