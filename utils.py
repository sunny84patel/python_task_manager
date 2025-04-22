from models import Task
from database import db

def create_task(name):
    task = Task(name=name)
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get(task_id)
