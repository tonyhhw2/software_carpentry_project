# To-Do App

This To-Do App is a simple and intuitive web application for managing daily tasks. It allows users to organize tasks by priority, set due dates, and customize the app's appearance through color themes.

## Features

1. **Task Management:**
   - Add new tasks with a title, priority (High, Medium, Low), and optional due date.
   - Mark tasks as complete or incomplete.
   - Delete tasks.

2. **Priority Levels:**
   - Tasks can be categorized as High, Medium, or Low priority.
   - Tasks are displayed in order of priority and due date.

3. **Due Dates:**
   - Users can specify due dates for their tasks.
   - Tasks are sorted by priority and due date.

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Jinja2 templates
- **Database:** SQLite (via SQLAlchemy)

## Prerequisites

- Python 3.x installed on your system
- pip package manager

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/to-do-app.git
   cd to-do-app
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Access the App:**
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. **Adding a Task:**
   - Fill out the task title, select a priority, and optionally set a due date.
   - Click "Add Task" to save the task.

2. **Marking a Task as Complete/Incomplete:**
   - Click on "Complete" or "Undo" to toggle the task's completion status.

3. **Deleting a Task:**
   - Click "Delete" to remove the task.

4. **Customizing Colors:**
   - Use the theme form to set background and text colors.
   - Click "Update Theme" to apply changes.

## Folder Structure

```
.
├── app.py          # Main application file
├── templates/
│   ├── index.html  # Frontend HTML template
├── static/
│   ├── style.css   # Custom styles (optional)
├── to_do.db        # SQLite database file (auto-generated)
└── README.md       # This readme file
```

## Future Improvements

- User authentication for private task lists.
- Task categorization by projects or tags.
- Notifications for upcoming due dates.
- Drag-and-drop task reordering.

## License

This project is licensed under the MIT License.

---

Enjoy staying organized with your new To-Do App!

