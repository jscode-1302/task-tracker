import json
from pathlib import Path

file = r'./tasks.json'

def command_help():
    print("\nadd 'task description'           → Create a new task")
    print("update <id> 'new description'    → Update an existing task")
    print("delete <id>                      → Delete a task")
    print("mark-in-progress <id>            → Mark task as in progress")
    print("mark-done <id>                   → Mark task as done")
    print("list                             → List all tasks")
    print("list 'status'                    → List tasks by status (e.g. 'done', 'in-progress')")

def load_data():
    if Path(file).exists: 
        try:
            with open(file, 'r') as f:
                existing_tasks = json.load(f)
                return existing_tasks
        except json.JSONDecodeError:
            return []
    return []
    
def get_max_id():
    tasks = load_data()
    if tasks:
        max_id = max([task['id'] for task in tasks])
        return max_id
    return 0
    
def next_id():
    max_id = get_max_id()
    return max_id + 1