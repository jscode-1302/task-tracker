# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks and to-do list. Built with Python, this project demonstrates fundamental programming concepts including file I/O, JSON data persistence, object-oriented programming, and CLI development.

## Features

- ✅ Add new tasks with descriptions
- ✏️ Update existing task descriptions
- 🗑️ Delete tasks by ID
- 📋 Mark tasks as in-progress or completed
- 📊 List all tasks or filter by status
- 💾 Persistent storage using JSON files
- 🔍 Input validation and error handling

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
1. Clone this repository:

git clone https://github.com/jscode-1302/task-tracker.git
cd task-tracker

2. Run the application:

python main.py

## Usage

The application runs in interactive mode. After starting, you'll see a welcome message and can enter commands.

### Available Commands

#### Adding Tasks

add 'Buy groceries'
Output: Task added successfully (ID: 1)

#### Updating Tasks

update 1 'Buy groceries and cook dinner'
Output: Task updated successfully!

#### Deleting Tasks

delete 1
Output: Task deleted successfully!

#### Marking Task Status

mark-in-progress 1
Output: Task marked in progress successfully!

mark-done 1
Output: Task marked done successfully!

#### Listing Tasks

List all tasks:
list

List tasks by status:
list todo
list in-progress
list done

#### Help

help
Displays all available commands and their usage

## Project Structure

task-tracker-cli/
│
├── main.py          # Main application entry point and CLI interface
├── models.py        # Task and TaskManager classes
├── utils.py         # Utility functions for data handling
├── tasks.json       # JSON file for persistent data storage (auto-generated)
└── README.md        # Project documentation

## Technical Details

### Classes

**Task Class:**
- Properties: id, description, status, created_at, updated_at
- Validation: Ensures task descriptions are at least 3 characters long
- String representations for easy display

**TaskManager Class:**
- Manages all task operations (CRUD)
- Handles JSON serialization/deserialization
- Automatic ID generation and file persistence

### Data Storage

Tasks are stored in tasks.json with the following structure:

[
    {
        "id": 1,
        "description": "Sample task",
        "status": "todo",
        "created_at": "22/06/2025",
        "updated_at": "22/06/2025"
    }
]

### Status Types
- todo - Default status for new tasks
- in-progress - Tasks currently being worked on
- done - Completed tasks

## Example Session

Welcome!
Enter 'help' to see the commands

add 'Learn Python OOP'
Task added successfully (ID: 1)

add 'Build a CLI app'
Task added successfully (ID: 2)

mark-in-progress 1
Task marked in progress successfully!

list
ID: 1 - Description: Learn Python OOP - Status: in-progress - Created at: 22/06/2025 - Updated at: 22/06/2025
ID: 2 - Description: Build a CLI app - Status: todo - Created at: 22/06/2025 - Updated at: 22/06/2025

mark-done 1
Task marked done successfully!

list done
ID: 1 - Description: Learn Python OOP - Status: done - Created at: 22/06/2025 - Updated at: 22/06/2025

## Key Features Implemented

- **Object-Oriented Design**: Clean separation between Task entities and TaskManager operations
- **Data Persistence**: JSON file storage with automatic loading/saving
- **Input Validation**: Regex-based command parsing with comprehensive error handling
- **User Experience**: Clear success/error messages and help documentation
- **Robust Error Handling**: Graceful handling of invalid inputs and edge cases

## Future Enhancements

- [ ] Add task priorities (high, medium, low)
- [ ] Implement due dates and reminders
- [ ] Add task categories/tags
- [ ] Export tasks to different formats (CSV, TXT)
- [ ] Add search functionality
- [ ] Implement task completion statistics

## Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/improvement)
3. Commit your changes (git commit -am 'Add some improvement')
4. Push to the branch (git push origin feature/improvement)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## About

This project was built as part of my journey learning Python and backend development. It demonstrates core programming concepts including:

- Object-oriented programming principles
- File I/O operations and JSON handling
- Regular expressions for input parsing
- Error handling and validation
- CLI application development

**Project inspired by:** roadmap.sh Task Tracker CLI Project
