# Task Tracker CLI

[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-windows%20|%20macOS%20|%20linux-lightgrey.svg)](https://github.com/jscode-1302/task-tracker)

A simple command-line interface (CLI) application to track and manage your tasks and to-do list. Built with Python, this project demonstrates fundamental programming concepts including file I/O, JSON data persistence, object-oriented programming, and CLI development.

## ✨ Features

- ✅ Add new tasks with descriptions
- ✏️ Update existing task descriptions
- 🗑️ Delete tasks by ID
- 📋 Mark tasks as in-progress or completed
- 📊 List all tasks or filter by status
- 💾 Persistent storage using JSON files
- 🔍 Input validation and error handling

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/jscode-1302/task-tracker.git
cd task-tracker

# Run the application
python main.py

# Add your first task
add 'Learn Python CLI development'
```

## 📋 Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: None (uses only Python standard library)

## 🛠️ Installation

### Method 1: Clone from GitHub

```bash
git clone https://github.com/jscode-1302/task-tracker.git
cd task-tracker
python main.py
```

### Method 2: Download ZIP

1. Download the ZIP file from the [repository](https://github.com/jscode-1302/task-tracker)
2. Extract to your desired location
3. Navigate to the folder in your terminal
4. Run `python main.py`

## 📖 Usage Guide

The application runs in interactive mode. After starting, you'll see a welcome message and can enter commands.

### 📝 Adding Tasks

```bash
add 'Buy groceries'
# Output: Task added successfully (ID: 1)

add 'Complete Python project'
# Output: Task added successfully (ID: 2)
```

### ✏️ Updating Tasks

```bash
update 1 'Buy groceries and cook dinner'
# Output: Task updated successfully!
```

### 🗑️ Deleting Tasks

```bash
delete 1
# Output: Task deleted successfully!
```

### 🏷️ Managing Task Status

```bash
# Mark as in progress
mark-in-progress 1
# Output: Task marked in progress successfully!

# Mark as completed
mark-done 1
# Output: Task marked done successfully!
```

### 📋 Viewing Tasks

```bash
# List all tasks
list

# List by status
list todo
list in-progress
list done
```

### 💡 Getting Help

```bash
help
# Shows all available commands and usage examples
```

## 💻 Example Session

```bash
Welcome!
Enter 'help' to see the commands

> add 'Learn Python OOP'
Task added successfully (ID: 1)

> add 'Build a CLI app'
Task added successfully (ID: 2)

> mark-in-progress 1
Task marked in progress successfully!

> list
ID: 1 - Description: Learn Python OOP - Status: in-progress - Created at: 01/07/2025 - Updated at: 01/07/2025
ID: 2 - Description: Build a CLI app - Status: todo - Created at: 01/07/2025 - Updated at: 01/07/2025

> mark-done 1
Task marked done successfully!

> list done
ID: 1 - Description: Learn Python OOP - Status: done - Created at: 01/07/2025 - Updated at: 01/07/2025
```

## 🏗️ Project Structure

```
task-tracker-cli/
│
├── main.py          # Main application entry point and CLI interface
├── models.py        # Task and TaskManager classes
├── utils.py         # Utility functions for data handling
├── tasks.json       # JSON file for persistent data storage (auto-generated)
├── .gitignore       # Git ignore rules
├── LICENSE          # MIT License
└── README.md        # Project documentation
```

## 🔧 Technical Details

### Core Classes

**Task Class**
- **Properties**: id, description, status, created_at, updated_at
- **Validation**: Ensures task descriptions are at least 3 characters long
- **Features**: Automatic timestamp management and string representations

**TaskManager Class**
- **Functionality**: Manages all task operations (CRUD)
- **Data Handling**: JSON serialization/deserialization
- **Features**: Automatic ID generation and file persistence

### Data Storage Format

Tasks are stored in `tasks.json` with this structure:

```json
[
    {
        "id": 1,
        "description": "Sample task",
        "status": "todo",
        "created_at": "01/07/2025",
        "updated_at": "01/07/2025"
    }
]
```

### Available Status Types

| Status | Description |
|--------|-------------|
| `todo` | Default status for new tasks |
| `in-progress` | Tasks currently being worked on |
| `done` | Completed tasks |

## 🛠️ Troubleshooting

**Common Issues:**

- **"Command not recognized"**: Make sure you're using the exact command format shown in `help`
- **"Invalid command or format"**: Check that task descriptions are enclosed in single quotes
- **"Id not found"**: Verify the task ID exists by running `list`
- **Python not found**: Ensure Python 3.7+ is installed and in your PATH

**File Issues:**
- The `tasks.json` file is created automatically on first use
- If the file becomes corrupted, delete it and restart the application

## 🎯 Key Programming Concepts Demonstrated

- **Object-Oriented Design**: Clean separation between Task entities and TaskManager operations
- **Data Persistence**: JSON file storage with automatic loading/saving
- **Input Validation**: Regex-based command parsing with comprehensive error handling
- **User Experience**: Clear success/error messages and help documentation
- **Error Handling**: Graceful handling of invalid inputs and edge cases

## 🚀 Future Enhancements

- [ ] Add task priorities (high, medium, low)
- [ ] Implement due dates and reminders
- [ ] Add task categories/tags
- [ ] Export tasks to different formats (CSV, TXT)
- [ ] Add search functionality
- [ ] Implement task completion statistics
- [ ] Add task dependencies
- [ ] Create a web interface version

## 🤝 Contributing

This is a learning project, but contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add some amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
git clone https://github.com/yourusername/task-tracker.git
cd task-tracker
# Make your changes
python main.py  # Test your changes
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 About This Project

This project was built as part of my journey learning Python and backend development. It demonstrates core programming concepts including:

- Object-oriented programming principles
- File I/O operations and JSON handling
- Regular expressions for input parsing
- Error handling and validation
- CLI application development

**Project inspired by:** [roadmap.sh Task Tracker CLI Project](https://roadmap.sh/projects/task-tracker)

---

⭐ **Found this helpful?** Give it a star on GitHub!