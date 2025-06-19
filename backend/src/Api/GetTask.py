from flask import Blueprint, jsonify
from BackEnd.src.todo.logic import get_task

get_task_bp = Blueprint('get_task', __name__)

@get_task_bp.route('/tasks/<int:index>', methods=['GET'])
def get_task_route(index):
    task = get_task(index)

    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify(task), 200
