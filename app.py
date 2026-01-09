import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from A_star import a_star_search
 
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-pathfinding", methods=["POST"])
def run():
    try:
        data = request.json
        grid = data["matrix"]
        start = tuple(data["start"])
        end = tuple(data["end"])

        grid[start[0]][start[1]] = 1
        grid[end[0]][end[1]] = 1

        visited, path = a_star_search(grid, start, end)

        return jsonify({"visited": visited, "path": path})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="10.15.101.67", port=5001, debug=True)