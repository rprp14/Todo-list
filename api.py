# proj/api.py
from ninja import Router, NinjaAPI
from .models import Task
from .schemas import TaskSchema, TaskUpdateSchema
from django.http import Http404

router = Router()
api = NinjaAPI()

@api.get("/tasks/", response=list[TaskSchema])
def list_tasks(request):
    tasks = Task.objects.all()
    return tasks

@api.post("/tasks", response=TaskSchema)
def create_task(request, task: TaskSchema):
    # Remove 'id' from the task dictionary since it's auto-generated
    task_dict = task.dict(exclude={"id"})
    task_obj = Task.objects.create(**task_dict)
    
    # Convert the Task instance to TaskSchema for the response
    return TaskSchema.from_orm(task_obj)

@api.get("/tasks/{task_id}", response=TaskSchema)
def get_task(request, task_id: int):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404
    return TaskSchema.from_orm(task)

@api.put("/tasks/{task_id}", response=TaskSchema)
def update_task(request, task_id: int, task: TaskUpdateSchema):
    try:
        task_obj = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404
    for attr, value in task.dict().items():
        setattr(task_obj, attr, value)
    task_obj.save()
    return TaskSchema.from_orm(task_obj)

@api.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404
    task.delete()
    return {"success": True}
