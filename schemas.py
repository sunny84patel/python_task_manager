from flask_marshmallow import Marshmallow
from models import Task

ma = Marshmallow()

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
