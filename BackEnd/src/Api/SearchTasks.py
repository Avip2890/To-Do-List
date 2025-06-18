from flask import Blueprint, request, jsonify
from BackEnd.src.todo.logic import search_tasks

search_tasks_bp = Blueprint('search_tasks', __name__)

@search_tasks_bp.route('/tasks/search', methods=['GET'])
def search_tasks_route():
    keyword = request.args.get('q', '')
    results = search_tasks(keyword)
    return jsonify(results)
