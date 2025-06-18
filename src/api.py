from flask import Flask
from flask_cors import CORS

# Blueprints
from Api.AddTask import add_task_bp
from Api.ListTasks import list_tasks_bp
from Api.DeleteTask import delete_task_bp
from Api.EditTask import edit_task_bp
from Api.MarkDone import mark_done_bp
from Api.SearchTasks import search_tasks_bp
from Api.ExportTasks import export_tasks_bp
from Api.GetTask import get_task_bp

app = Flask(__name__)

# CORS הגדרה נכונה ומקיפה
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# רישום כל ה־Blueprints
app.register_blueprint(add_task_bp)
app.register_blueprint(list_tasks_bp)
app.register_blueprint(delete_task_bp)
app.register_blueprint(edit_task_bp)
app.register_blueprint(mark_done_bp)
app.register_blueprint(search_tasks_bp)
app.register_blueprint(export_tasks_bp)
app.register_blueprint(get_task_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
