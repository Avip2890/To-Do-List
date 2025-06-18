from flask import Blueprint, request, jsonify
from src.todo.logic import load_tasks

list_tasks_bp = Blueprint('list_tasks', __name__)
@list_tasks_bp.route('/tasks', methods=['GET'])
def list_tasks_route():
    tasks = load_tasks()
    return jsonify(tasks), 200

