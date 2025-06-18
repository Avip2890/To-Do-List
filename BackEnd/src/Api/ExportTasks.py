from flask import Blueprint, jsonify
from BackEnd.src.todo.logic import export_tasks

export_tasks_bp = Blueprint('export_tasks', __name__)

@export_tasks_bp.route('/tasks/export', methods=['GET'])
def export_tasks_route():
    result = export_tasks()
    return jsonify({'message': 'Tasks exported successfully', 'details': result})
