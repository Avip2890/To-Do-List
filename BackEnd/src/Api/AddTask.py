from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from BackEnd.src.todo.logic import add_task

add_task_bp = Blueprint('add_task', __name__, url_prefix='/tasks')

@add_task_bp.route('/add', methods=['POST', 'OPTIONS'])
@cross_origin(origin='http://localhost:5173')  # או origins="*"
def add_task_route():
    data = request.get_json()
    task_text = data.get("task")
    deadline = data.get("deadline")
    priority = data.get("priority", 1)
    tags = data.get("tags", [])  # ← זה מה שהיה חסר

    if not task_text:
        return jsonify({"error": "חסר טקסט משימה"}), 400

    new_task = add_task(task_text, deadline, priority, tags)  # ← תעביר גם לפונקציה
    return jsonify(new_task), 201
