from datetime import datetime
from utils import load_data, next_id
import json

file = r'./tasks.json'

class Task:
    def __init__(self, id, description, status='todo', created_at=None, updated_at=None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if len(value) < 3:
            raise ValueError('Please enter a valid description')
        self._description = value
        
    def __str__(self):
        return f"ID: {self.id} - Description: {self.description} - Status: {self.status} - Created at: {self.created_at.strftime('%d/%m/%Y')} - Updated at: {self.updated_at.strftime('%d/%m/%Y')}"
    
    def __repr__(self):
        return f"Task({self.id}, {self.description}, {self.status}, {self.created_at}, {self.updated_at})"
        
class TaskManager:    
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, description):
        id_count = next_id()
        try:
            task = Task(id_count, description)
        except ValueError as e:
            print(f"An error has ocurred: {e}")
            return False
        
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task.id})")
        return True
        
    def update_task(self, id, new_description):
        for task in self.tasks:
            if id == task.id:
                try:
                    task.description = new_description
                except ValueError as e:
                    print(f"An error has ocurred: {e}")
                    return False
                task.updated_at = datetime.now()
                self.save_tasks()
                print("Task updated successfully!")
                return True
        print('Id not found')
        return False
        
    def delete_task(self, id):
        for index, task in enumerate(self.tasks):
            if id == task.id:
                del self.tasks[index]
                self.save_tasks()
                print("Task deleted successfully!")
                return True
        print('Id not found')
        return False
    
    def mark_in_progress(self, id):
        for task in self.tasks:
            if id == task.id:
                task.status = 'in-progress'
                task.updated_at = datetime.now()
                self.save_tasks()
                print("Task marked in progress successfully!")
                return True
        print('Id not found')
        return False
    
    def mark_done(self, id):
        for task in self.tasks:
            if id == task.id:
                task.status = 'done'
                task.updated_at = datetime.now()
                self.save_tasks()
                print("Task marked done successfully!")
                return True
        print('Id not found')
        return False
    
    def display_tasks_by_status(self, status):
        if self.tasks:
            tasks = list(filter(lambda x: x.status == status, self.tasks))
            return tasks
        return []
    
    def to_dict(self):
        tasks_list = []
        if self.tasks:
            for task in self.tasks:
                tasks_list.append({
                    'id': task.id,
                    'description': task.description,
                    'status': task.status,
                    'created_at': datetime.strftime(task.created_at, "%d/%m/%Y"),
                    'updated_at': datetime.strftime(task.updated_at, "%d/%m/%Y")
                })
                
        return tasks_list
    
    def save_tasks(self):
        tasks = self.to_dict()
        with open(file, 'w') as f:
            json.dump(tasks, f, indent=4)
            return True
        
    def load_tasks(self):
        self.tasks = []
        data = load_data()
        if data:
            for task in data:
                self.tasks.append(Task(
                    task['id'],
                    task['description'],
                    task['status'],
                    datetime.strptime(task['created_at'], "%d/%m/%Y"),
                    datetime.strptime(task['updated_at'], "%d/%m/%Y")
                ))
            return True
        
                 
        
        
        