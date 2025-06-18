from flask import Blueprint, request, jsonify
from BackEnd.src.todo.logic import edit_task

edit_task_bp = Blueprint('edit_task', __name__)

@edit_task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task_route(task_id):
    data = request.json
    text = data.get("task")
    deadline = data.get("deadline")
    done = data.get("done")  # ← ודא שאתה לוקח גם את done

    updated = edit_task(task_id, text, deadline, done)
    if updated:
        return jsonify(updated), 200
    else:
        return jsonify({"error": "Task not found"}), 404
