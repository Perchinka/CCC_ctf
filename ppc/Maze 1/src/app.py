from maze import generate_maze, possible_moves, move
from flask import Flask, render_template, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 

@app.route('/')
def index():
    if 'maze' not in session:
        session['maze'], session['coords'], session['end'] = generate_maze()

    return render_template('maze.html', current=session['coords'] ,end=session['end'])

@app.route('/move/<direction>', methods=['POST'])
def move_direction(direction):
    if 'maze' not in session:
        return jsonify({"success": False, "message": "No maze found for this session"})

    maze = session['maze']
    coords = session['coords']
    end = session['end']

    possible = possible_moves(maze, coords[1], coords[0])
    
    if direction in possible and possible[direction]:
        new_x, new_y = move(maze, coords[1], coords[0], direction)
        session['coords'] = (new_y, new_x)
        if new_y == end[0] and new_x == end[1]:
            return jsonify({"success": True, "message": "CCC{y0u_4r3_4_m4z3_m4573r!}"})
        return jsonify({"success": True, "message": "Moved successfully"})
    else:
        return jsonify({"success": False, "message": "Invalid move"})


@app.route('/possible_moves', methods=['POST'])
def get_possible_moves():
    if 'maze' not in session:
        return jsonify({"success": False, "message": "No maze found for this session"})

    maze = session['maze']
    coords = session['coords']

    return jsonify({"success": True, "moves": possible_moves(maze, coords[1], coords[0])})


@app.route('/get_coordinates', methods=['GET'])
def get_coordinates():
    if 'maze' not in session:
        return jsonify({"success": False, "message": "No maze found for this session"})

    coords = session['coords']
    end = session['end']

    return jsonify({"success": True, "current": coords, "end": end})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)