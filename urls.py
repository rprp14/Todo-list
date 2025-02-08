from django.urls import path
from ninja import NinjaAPI
from .views import router as task_router
from .schemas import TaskSchema 

api = NinjaAPI()

api.add_router("/api/", task_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api", api.urls),
]
@api.get("/tasks/", response=list[TaskSchema])  # Specify that the response is a list of TaskSchema
def list_tasks(request):
    tasks = Task.objects.all()
    return tasks 
