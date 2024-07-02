from flask import Flask, request, jsonify, session, render_template
from alphabeta_minimax import computer_move

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_best_move', methods=['POST'])
def calculate_best_move():
    data = request.json
    current_number = data['currentNumber']
    algorithm = data['algorithm']
    
    best_move = computer_move(current_number, algorithm)

    return jsonify(best_move=best_move)

if __name__ == '__main__':
    app.run(debug=True)