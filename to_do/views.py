from django.shortcuts import render
from .models import TodoList, Category
from django.contrib import messages


def views(request):
    return render(request, "index.html")


def addtasks(request):
    categories = Category.objects.all()

    return render(request, "addtasks.html", {"categories": categories})


def viewtask(request):
    todos = TodoList.objects.all()
    return render(request, "show task.html", {"todos": todos})


def savetask(request):
    title = request.POST["description"]
    date = str(request.POST["date"])
    category = request.POST["category_select"]
    content = title + " -- " + date + " " + category
    if request.POST == None:
        categories = Category.objects.all()
        Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
        Todo.save()
        messages.add_message(request, messages.INFO, 'Task Successfully Added')
        return render(request, "addtasks.html", {"categories": categories})
    id = request.POST["todo_id"]
    TodoList.objects.filter(id=id).update(title=title, content=content, due_date=date,
                                          category=Category.objects.get(name=category))
    todos = TodoList.objects.all()
    messages.add_message(request, messages.INFO, 'Task Successfully Updated')
    return render(request, "show task.html", {"todos": todos})


def deletetask(request):
    todo_id = request.POST.get("delete")
    todo = TodoList.objects.get(id=int(todo_id))
    todo.delete()
    messages.add_message(request, messages.INFO, 'Task Successfully deleted')
    todos = TodoList.objects.all()
    return render(request, "show task.html", {"todos": todos})


def updatetask(request):
    todo_id = request.POST.get("update")
    todo = TodoList.objects.get(id=int(todo_id))
    categories = Category.objects.all()
    return render(request, "addtasks.html", {"categories": categories, "todo": todo, "todo_id": todo_id})
