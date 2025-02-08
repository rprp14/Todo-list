from ninja import Router
from .models import Task
from .schemas import TaskIn, TaskOut
from django.http import Http404
# views.py


router = Router()

# Create a new task
@router.post("/tasks", response=TaskOut)
def create_task(request, task_in: TaskIn):
    task = Task.objects.create(**task_in.dict())
    return task

# List all tasks
@router.get("/tasks", response=list[TaskOut])
def list_tasks(request):
    return Task.objects.all()

# Get a single task
@router.get("/tasks/{task_id}", response=TaskOut)
def get_task(request, task_id: int):
    try:
        return Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404

# Update a task
@router.put("/tasks/{task_id}", response=TaskOut)
def update_task(request, task_id: int, task_in: TaskIn):
    try:
        task = Task.objects.get(id=task_id)
        for attr, value in task_in.dict().items():
            setattr(task, attr, value)
        task.save()
        return task
    except Task.DoesNotExist:
        raise Http404

# Delete a task
@router.delete("/tasks/{task_id}", response={204: None})
def delete_task(request, task_id: int):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return 204, None
    except Task.DoesNotExist:
        raise Http404
