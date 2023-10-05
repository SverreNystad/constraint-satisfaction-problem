document.addEventListener("DOMContentLoaded", () => {
    const board = document.getElementById('sudoku-board');
    for (let i = 0; i < 9; i++) {
        const row = board.insertRow(i);
        for (let j = 0; j < 9; j++) {
            const cell = row.insertCell(j);

            cell.contentEditable = true;
            cell.addEventListener('keydown', handleInput);
            cell.addEventListener('input', handleMaxSize);
        }
    }
});

function handleInput(event) {
    // Allow navigation keys
    if (event.key === "Backspace" || event.key === "ArrowRight" || event.key === "ArrowLeft" || event.key === "ArrowUp" || event.key === "ArrowDown" || event.key === "Delete") {
        return true;
    }
    
    // Check if the key pressed is a digit 1-9
    if (!/^[1-9]$/.test(event.key)) {
        // If not, prevent the input
        event.preventDefault();
    }

}

function handleMaxSize(event) {
    // Prevent the user from entering more than one character
    if (event.target.innerText.length > 1) {
        event.target.innerText = event.target.innerText[0];
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const solveButton = document.getElementById('solve-button');
    solveButton.addEventListener('click', function() {
        const boardArray = getBoardAsArray();
        sendBoardToServer(boardArray);
    });
});

function getBoardAsArray() {
    const board = document.getElementById('sudoku-board');
    const boardArray = Array.from(board.rows).map(row => 
        Array.from(row.cells).map(cell => cell.innerText || '')
    );
    return boardArray;
}

// Reset the board to empty
document.addEventListener("DOMContentLoaded", () => {
    const clearButton = document.getElementById('clear-button');
    clearButton.addEventListener('click', function() {
        const board = document.getElementById('sudoku-board');
        for (let i = 0; i < 9; i++) {
            const row = board.rows[i];
            for (let j = 0; j < 9; j++) {
                const cell = row.cells[j];
                cell.innerText = '';
            }
        }
    });
});

function sendBoardToServer(boardArray) {
    showLoading();  // Show loading spinner when sending request
    resetErrorMessage();
    fetch('/solve', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({board: boardArray})
    })
    .then(response => {
        if (!response.ok) {
            updateErrorMessage();
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        hideLoading();  // Hide loading spinner when response is received

        console.log('Received data:', data);  // Add this line to log received data
        if (data.error) {
            alert(data.error);
            return;
        }
        const stats = data.stats;
        updateStats(stats);
        const solution = data.solution;
        updateBoard(solution);
        
    })
    .catch(error => {
        hideLoading();  // Hide loading spinner if an error occurs
        console.error('Fetch error:', error);
    });
}

function showLoading() {
    document.getElementById('loading').classList.remove('loading-hidden');
    document.getElementById('loading').classList.add('loading-visible');
}

function hideLoading() {
    document.getElementById('loading').classList.remove('loading-visible');
    document.getElementById('loading').classList.add('loading-hidden');
}

function updateErrorMessage() {
    const errorMessage = document.getElementById('error-message');
    errorMessage.innerText = 'Error: Invalid board';
}

function resetErrorMessage() {
    const errorMessage = document.getElementById('error-message');
    errorMessage.innerText = '';
}

function updateStats(stats) {
    console.log("Updating stats with:", stats);
    // stats is a dictionary with the following keys: backtrack_attempts, failures
    const statsElement = document.getElementById('stats');
    statsElement.innerText = `Backtrack attempts: ${stats.backtrack_attempts}, failures: ${stats.failures}`;

}

function updateBoard(solution) {
    console.log("Updating board with:", solution);
    const board = document.getElementById('sudoku-board');
    for (let i = 0; i < 9; i++) {
        const row = board.rows[i];
        for (let j = 0; j < 9; j++) {
            const key = `${i}-${j}`;
            const value = solution[key];

            if (value && value[0] !== undefined) {
                const cell = row.cells[j];
                cell.innerText = value[0];
            } else {
                console.error(`Undefined value at solution[${key}]`);
            }
        }
    }
}
