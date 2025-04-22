from flask import Flask, jsonify, request, render_template
from datetime import datetime

app = Flask(__name__)
tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json(force=True)
    if not data or 'name' not in data or not data['name'].strip():
        return jsonify({'error': 'Missing or empty "name" field'}), 400

    new_task = {
        'id': task_id_counter,
        'name': data['name'].strip(),
        'status': 'running',
        'created_at': datetime.utcnow().isoformat()
    }
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({'error': f'Task {task_id} not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        tasks = [t for t in tasks if t['id'] != task_id]
        return jsonify({'message': f'Task {task_id} deleted'}), 200
    return jsonify({'error': f'Task {task_id} not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
