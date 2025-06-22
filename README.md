# Bug Tracker Web App

# Description
A web-based bug/issue tracking application built with Python and Flask. Users can create, view, update, and delete bugs with assigned priorities, statuses, and assignees. It helps small teams track and manage software bugs efficiently.

# Features
- Add, update, and delete bugs
- Assign status (Open, In Progress, Resolved)
- Set priority (High, Medium, Low)
- Assign to specific users
- View all bugs in a table layout

# Technologies
- Python 3.x
- Flask
- SQLite (built-in)
- HTML, CSS (for UI)

# Getting Started

# Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

Install dependencies
pip install flask

Run the app
python app.py

Then open:
http://127.0.0.1:5000
Requirements
flask

SQLite will be auto-initialized (bug_tracker.db) on first run.
