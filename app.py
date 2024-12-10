from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(50), nullable=False, default="medium")
    due_date = db.Column(db.DateTime, nullable=True)

with app.app_context():
    db.create_all()

# Route for displaying tasks
@app.route('/')
def index():
    tasks = Task.query.order_by(
        db.case(
            (Task.priority == "high", 1),
            (Task.priority == "medium", 2),
            (Task.priority == "low", 3),
        ),
        Task.due_date.asc()  # Sort by due date after priority
    ).all()
    color_theme = session.get("color_theme", {"bg_color": "#f4f4f9", "text_color": "#333"})
    return render_template('index.html', tasks=tasks, color_theme=color_theme)

# Route for adding a new task
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    priority = request.form.get('priority')
    due_date = request.form.get('due_date')
    if title and priority:
        new_task = Task(
            title=title,
            priority=priority,
            due_date=datetime.strptime(due_date, '%Y-%m-%d') if due_date else None
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

# Route for toggling task completion
@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.complete = not task.complete
        db.session.commit()
    return redirect(url_for('index'))

# Route for deleting a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

# Route for updating color theme
@app.route('/update_color', methods=['POST'])
def update_color():
    bg_color = request.form.get("bg_color")
    text_color = request.form.get("text_color")
    if bg_color and text_color:
        session["color_theme"] = {"bg_color": bg_color, "text_color": text_color}
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
