from flask import Blueprint, jsonify
from src.todo.logic import delete_task

delete_task_bp = Blueprint('delete_task', __name__)

@delete_task_bp.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task_route(index):
    deleted = delete_task(index)

    if deleted is None:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify({'message': 'Task deleted successfully', 'task': deleted}), 200





