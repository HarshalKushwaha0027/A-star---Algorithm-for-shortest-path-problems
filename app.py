from flask import Flask, request, jsonify
from flask_cors import CORS
from A_star import a_star_search

app = Flask(__name__)
CORS(app)

@app.route("/run-pathfinding", methods=["POST"])
def run():
    try:
        data = request.json

        print("REQUEST RECEIVED")
        print("Start:", data["start"], "End:", data["end"])

        grid = data["matrix"]
        start = tuple(data["start"])
        end = tuple(data["end"])

        # force start/end to be traversable
        grid[start[0]][start[1]] = 1
        grid[end[0]][end[1]] = 1

        visited, path = a_star_search(grid, start, end)

        print("Visited:", len(visited), "Path:", len(path))

        return jsonify({
            "visited": visited,
            "path": path
        })

    except Exception as e:
        print("BACKEND ERROR:", e)
        return jsonify({"error": str(e)}), 500


@app.route("/")
def health():
    return "Backend is running"


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
