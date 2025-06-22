from utils import command_help
from models import TaskManager
import re

def main():
    print("Welcome!\nEnter 'help' to see the commands")
    
    commands_allowed = ['dict','help', 'add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']
    
    tm = TaskManager()
    
    while True:
        user_input = input('\n')
        user_input_list = user_input.split()
        
        if user_input_list[0] not in commands_allowed:
            print('Command not recognize')
        
        # displaying help
        elif user_input_list[0].lower().strip() == 'help':
            command_help()
        
        # adding a new task   
        elif user_input_list[0].lower().strip() == 'add':
            pattern_match = re.fullmatch(r"(add)\s+('[^']+'\s*)", user_input)
            if not pattern_match:
                print('Invalid command or format. Type \'help\' to look at the valid commands.')
            else:
                task = pattern_match.group(2)
                tm.add_task(task[1:-1].strip())
        
        # updating a task         
        elif user_input_list[0].lower().strip() == 'update':
            pattern_match = re.fullmatch(r"(update)\s+([1-9]+)\s+('[^']+'\s*)", user_input)
            if not pattern_match:
                print('Invalid command or format. Type \'help\' to look at the valid commands.')
            else:
                id = pattern_match.group(2)
                description = pattern_match.group(3)
                tm.update_task(int(id), description[1:-1].strip())

        # deleting a taks
        elif user_input_list[0].lower().strip() == 'delete':
            pattern_match = re.fullmatch(r'(delete)\s+([1-9]+\s*)', user_input)
            if not pattern_match:
                print('Invalid command or format. Type \'help\' to look at the valid commands.')
            else:
                id = pattern_match.group(2)
                tm.delete_task(int(id))
                
        # marking a task as in-progress
        elif user_input_list[0].lower().strip() == 'mark-in-progress':
            pattern_match = re.fullmatch(r'(mark-in-progress)\s+([1-9]+\s*)', user_input)
            if not pattern_match:
                print('Invalid command or format. Type \'help\' to look at the valid commands.')
            else:
                id = pattern_match.group(2)
                tm.mark_in_progress(int(id))
                
        # marking a task as done
        elif user_input_list[0].lower().strip() == 'mark-done':
            pattern_match = re.fullmatch(r'(mark-done)\s+([1-9]+\s*)', user_input)
            if not pattern_match:
                print('Invalid command or format. Type \'help\' to look at the valid commands.')
            else:
                id = pattern_match.group(2)
                tm.mark_done(int(id))
                
        # listing all tasks
        elif user_input_list[0].lower().strip() == 'list':
            pattern_match = re.fullmatch(r'(list)(\s(todo|done|in-progress))?\s*', user_input)
            valid_status = ['todo', 'done', 'in-progress']
            
            if not pattern_match:
                print('Invalid command or format. Type \'help\' to look at the valid commands.')
            else:
                if pattern_match.group(3) is None:  
                    tasks = tm.tasks
                    for task in tasks:
                        print(f"ID: {task.id} - Description: {task.description} - Status: {task.status} - Created at: {task.created_at} - Updated at: {task.updated_at}")
                elif pattern_match.group(3) in valid_status:
                    status = pattern_match.group(3)
                    tasks = tm.display_tasks_by_status(status)
                    for task in tasks:
                        print(f"ID: {task.id} - Description: {task.description} - Status: {task.status} - Created at: {task.created_at} - Updated at: {task.updated_at}")
                else:
                    print('Status not valid')

if __name__ == '__main__':
    main()