url = "http://127.0.0.1:5000/tasks"
task = {"task": "לסיים את הפרויקט"}

response = requests.post(url, json=task)

print(response.status_code)
print(response.json())

