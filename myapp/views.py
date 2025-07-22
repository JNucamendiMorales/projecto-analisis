from django.http import HttpResponse, JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404, render,redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
    title="Reservaciones chuilaquiles Airbnb"
    return render(request, "index.html",{
        "mostrarTitulo": title
    })


def about(request):
    username="Nuca_29"
    age="28"
    numbers={
        "luckyNumber":3
    }
    return render(request, "about.html",{
        "mostrarUsername":username,
        "mostrarAge":age,
        "favNumbers":numbers
    })


def projects(request):
    #projects = list (Project.objects.values())
    projects=Project.objects.all()
    return render (request, "projects/projects.html",{
        "showAllProjects":projects
    })


def tasks(request):
    #task = get_object_or_404(Task, title=title)
    tasks=Task.objects.all()
    return render (request, "tasks/tasks.html",{
        "showAllTasks":tasks
    })


def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s </h2>" % username)

def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html",{
        "form" : CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST["title"], description=request.POST["description"],project_id=1)
        return redirect("/tasks/")
    

def create_project(request):
    if request.method == "GET":
        return render (request, "projects/create_project.html",{
        "form" : CreateNewProject()
    })
    else:
        project=Project.objects.create(name=request.POST["name"])
        print(project)
        return render (request, "projects/create_project.html",{
        "form" : CreateNewProject()
    })







