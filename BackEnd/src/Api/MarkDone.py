from flask import Blueprint, jsonify
from BackEnd.src.todo.logic import mark_task_done

mark_done_bp = Blueprint('mark_done', __name__)

@mark_done_bp.route('/tasks/<int:index>/done', methods=['PATCH'])
def mark_done_route(index):
    updated_task = mark_task_done(index)

    if updated_task is None:
        return jsonify({'error': 'Invalid index'}), 400

    return jsonify(updated_task), 200
