from flask import Flask, render_template, request, jsonify
from src.sudoku_solver.sudoku_utils import create_sudoku_csp_from_array

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    # Get board from JSON data
    data = request.get_json()
    board = data.get('board')
    print(f"board = {board}")
    csp = create_sudoku_csp_from_array(board)
    solution = csp.backtracking_search()
    csp.print_stats()
    
    # Check if the solution is valid
    for i in range(9):
        for j in range(9):
            key = f"{i}-{j}"
            if key not in solution or not isinstance(solution[key], list) or len(solution[key]) != 1:
                return jsonify({'error': f'Invalid solution format at {key}'}), 500

    # Respond with the solution
    return jsonify({'solution': solution, 'stats': csp.get_stats()}), 200

if __name__ == "__main__":
    app.run(debug=True)
