import json
import random
from datetime import datetime

FILENAME = "tasks.json"

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []



def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def generate_numeric_id(existing_ids):
    while True:
        new_id = random.randint(100, 999)
        if new_id not in existing_ids:
            return new_id

def add_task(task_text, deadline=None, priority="medium", tags=None):
    tasks = load_tasks()

    existing_ids = [task.get("id") for task in tasks]
    new_id = generate_numeric_id(existing_ids)

    if not deadline:
        deadline = "ללא"
    if tags is None:
        tags = []

    new_task = {
        "id": new_id,
        "task": task_text,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deadline": deadline,
        "priority": priority,
        "tags": tags
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task
def add_task(task_text, deadline=None, priority="medium",tags=None):
    tasks = load_tasks()

    existing_ids = [task.get("id") for task in tasks]
    new_id = generate_numeric_id(existing_ids)

    if not deadline:
        deadline = "ללא"

    new_task = {
        "id": new_id,
        "task": task_text,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deadline": deadline,
        "priority": priority,
        "tags": tags
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task


def list_tasks():
    return load_tasks()

def search_tasks(keyword):
    tasks = load_tasks()
    keyword = keyword.lower()
    return [task for task in tasks if keyword in task["task"].lower()]

def mark_task_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            return removed
    return None

def edit_task(task_id, new_text=None, deadline=None, done=None,tags=None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if new_text is not None:
                task["task"] = new_text
            if deadline is not None:
                task["deadline"] = deadline
            if done is not None:
                task["done"] = done
            if tags is not None:
                task["tags"] = tags
                save_tasks(tasks)
            save_tasks(tasks)
            return task
    return None



def export_tasks(filepath="report.txt"):
    tasks = load_tasks()
    if not tasks:
        return "אין משימות לייצא."

    with open(filepath, "w", encoding="utf-8-sig") as file:
        file.write("דו\"ח משימות:\n\n")
        for i, t in enumerate(tasks, 1):
            status = "בוצע" if t["done"] else "לא בוצע"
            created = t.get("created", "לא ידוע")
            deadline = t.get("deadline", "ללא")
            priority = t.get("priority", "medium")
            file.write(f"{i}. {t['task']}\n")
            file.write(f"   סטטוס: {status}\n")
            file.write(f"   נוצר בתאריך: {created}\n")
            file.write(f"   תאריך יעד: {deadline}\n\n")
            file.write(f"   עדיפות: {priority}\n\n")

    return f"דו\"ח נוצר בהצלחה בקובץ '{filepath}'"

def get_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None
