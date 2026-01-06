const canvas = document.getElementById("gridCanvas");
const ctx = canvas.getContext("2d");

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


let ROWS = 20;
let COLS = 20;
let CELL_SIZE = canvas.width / COLS;

let mode = "obstacle";

let grid = Array.from({ length: ROWS }, () =>
    Array(COLS).fill(1)
);
function initGrid(size) {
    ROWS = size;
    COLS = size;
    CELL_SIZE = canvas.width / COLS;

    grid = Array.from({ length: ROWS }, () =>
        Array(COLS).fill(1)
    );

    start = null;
    end = null;
    drawGrid();
}

document.getElementById("gridSize").onchange = (e) => {
    initGrid(parseInt(e.target.value));
};


let start = null;
let end = null;
function drawGrid() {
    // 1. Clear the canvas with the background color
    ctx.fillStyle = "#0b0c10"; // Matches your Body BG
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            
            // Default styling for "Empty Cell" (Normal Weight)
            let color = "#1f2833"; // Dark Grey (Tech feel)
            // Determine Color based on Grid Value
            if (grid[r][c] === 0) {
                color = "#000000"; // <--- CHANGED TO PURE BLACK (Obstacle)
            } else if (grid[r][c] === 1) {
                color = "#1f2833"; // Normal: Dark Grey
            } else if (grid[r][c] <= 3) {
                color = "#2c3e50"; // Weight 2: Slightly lighter blue-grey
            } else if (grid[r][c] <= 6) {
                color = "#3a506b"; // Weight 5: Deep Blue
            } else {
                color = "#5c258d"; // Weight 10: Deep Purple (High cost)
            }

            // Draw the cell
            ctx.fillStyle = color;
            
            // THE TRICK: Draw slightly smaller squares to create "Grid Lines" naturally
            // (x + 1, y + 1, width - 2, height - 2)
            ctx.fillRect(c * CELL_SIZE + 1, r * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2);
        }
    }

    // Draw Start and End on top (Neon colors)
    if (start) paintCell(start, "#39ff14", "Start"); // Neon Green
    if (end) paintCell(end, "#ff073a", "End");     // Neon Red
}

function paintCell([r, c], color) {
    ctx.fillStyle = color;
    // Keep the same "gap" logic (+1, -2)
    ctx.fillRect(c * CELL_SIZE + 1, r * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2);
    
    // Optional: Add a "Shadow/Glow" for important cells (Start/End)
    // Note: Canvas shadows can be performance heavy on huge grids, but fine for 20x20
    ctx.shadowBlur = 0; 
}

function generateDummySteps() {
    let visited = [];
    let path = [];

    // simple straight-line simulation
    let r = start[0];
    let c = start[1];

    while (r !== end[0] || c !== end[1]) {
        visited.push([r, c]);

        if (r < end[0]) r++;
        else if (c < end[1]) c++;
        else if (r > end[0]) r--;
        else if (c > end[1]) c--;
    }

    visited.push(end);
    path = [...visited];

    return { visited, path };
}

async function animatePath(visited, path) {
    // 1. Animate Visited Nodes (Scanner Effect)
    for (let cell of visited) {
        let [r, c] = cell;

        // Skip start/end to keep them visible
        if ((start[0] === r && start[1] === c) || (end[0] === r && end[1] === c)) continue;

        // Color: Transparent Neon Cyan (So you can see if it was a weighted node underneath)
        ctx.fillStyle = "rgba(102, 252, 241, 0.6)"; 
        ctx.fillRect(c * CELL_SIZE + 1, r * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2);

        // Faster animation for smoother feel
        await sleep(10); 
    }

    // 2. Animate Shortest Path (The Result)
    for (let cell of path) {
        let [r, c] = cell;

        if ((start[0] === r && start[1] === c) || (end[0] === r && end[1] === c)) continue;

        // Color: Bright Gold/Yellow
        ctx.fillStyle = "#fdd835"; 
        ctx.fillRect(c * CELL_SIZE + 1, r * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2);

        await sleep(30);
    }
}

canvas.addEventListener("click", e => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const r = Math.floor(y / CELL_SIZE);
    const c = Math.floor(x / CELL_SIZE);

    if (
        (start && r === start[0] && c === start[1]) ||
        (end && r === end[0] && c === end[1])
    ) {
        grid[r][c] = 1;
    }


    if (mode === "obstacle") {
        const weight = parseInt(
            document.getElementById("weightMode").value
        );
        grid[r][c] = weight;
    }

    else if (mode === "start") {
        start = [r, c];
    } 
    else if (mode === "end") {
        end = [r, c];
    }

    drawGrid();
});
document.getElementById("drawObstacle").onclick = () => mode = "obstacle";
document.getElementById("setStart").onclick = () => mode = "start";
document.getElementById("setEnd").onclick = () => mode = "end";

document.getElementById("clearGrid").onclick = () => {
    grid = Array.from({ length: ROWS }, () =>
        Array(COLS).fill(1)
    );
    start = null;
    end = null;
    drawGrid();
};


document.getElementById("randomGrid").onclick = () => {
    const weights = [0, 1, 2, 5, 10];

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            grid[r][c] = weights[Math.floor(Math.random() * weights.length)];
        }
    }
    drawGrid();
};

document.getElementById("runAlgo").onclick = async () => {

    if (!start || !end) {
        alert("Please select start and end points");
        return;
    }

    drawGrid(); // reset visualization

    const response = await fetch("http://localhost:5001/run-pathfinding", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            matrix: grid,
            start: start,
            end: end
        })
    });

    
    const data = await response.json();

    document.getElementById("nodesVisited").innerText = data.visited.length;
    document.getElementById("pathLength").innerText = data.path.length;
    document.getElementById("statusText").innerText = "Completed";
    document.getElementById("statusText").style.color = "#66fcf1"; // Cyan color

    console.log("Visited:", data.visited.length);
    console.log("Path:", data.path.length);

    await animatePath(data.visited, data.path);
};


initGrid(20);

