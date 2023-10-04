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
    // Allow navigation keys: backspace, left, and right
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