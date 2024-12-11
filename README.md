# Flask To-Do App with User Authentication

This is a simple yet robust **To-Do List Application** built using **Flask**. It supports user authentication and personalized task management. Each user has their own private task list with features like task prioritization, due dates, and completion toggles.

---

## Features

- **User Authentication**: Secure registration and login system using hashed passwords.
- **Task Management**:
  - Add, edit, and delete tasks.
  - Set task priority levels: High, Medium, and Low.
  - Add a due date for tasks.
  - Mark tasks as complete or incomplete.
- **Responsive and Clean Design**: Styled with CSS for a professional appearance.

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/flask-todo-app.git
    cd flask-todo-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

6. Open your browser and go to:
    ```
    http://127.0.0.1:5000
    ```

---

## File Structure

flask-todo-app/ ├── static/ │ └── styles.css # Custom CSS for styling ├── templates/ │ ├── index.html # Main page for tasks │ ├── login.html # Login page │ ├── register.html # Registration page ├── app.py # Main application file ├── requirements.txt # Python dependencies ├── README.md # Project documentation └── to_do.db # SQLite database (auto-generated)


---

## Usage

### User Authentication
- **Register**: Create a new account with a unique username and password.
- **Login**: Access your private to-do list after logging in.
- **Logout**: Log out securely from the app.

### Task Management
- **Add a Task**: Input the task title, select a priority (High, Medium, Low), and optionally set a due date.
- **Mark as Complete**: Toggle task completion.
- **Delete a Task**: Remove unwanted tasks.

---

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Authentication**: Password hashing with `werkzeug.security`

---

## Screenshots

### Login Page
![Login Page](https://via.placeholder.com/800x400?text=Login+Page)

### Task List
![Task List](https://via.placeholder.com/800x400?text=Task+List)

---

## Future Enhancements

- Add task editing functionality.
- Implement reminders and notifications for due dates.
- Extend UI responsiveness for better mobile compatibility.

---

## License

This project is licensed under the [MIT License](LICENSE).
