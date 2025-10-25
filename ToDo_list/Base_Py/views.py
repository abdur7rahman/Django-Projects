from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib.auth.views import LoginView
# from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Tasks
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def LoginResponse(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if User.objects.filter(username=username).exists():
            if user:
                login(request,user)
                return redirect('taskspage')
            else:
                messages.error(request,"password is incorrect")
        else:
            messages.error(request,"username is not exist")
        
    return render(request, "login.html")

# def LoginResponse(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password):
#                 request.session['user_id'] = user.id
#                 return redirect('taskspage')
#             else:
#                 error = "Wrong Password"

#         except Exception as e:
#             error = e

#         return render(request, 'login.html', context={'error':error})
    
#     return render(request, 'login.html')

def LogoutResponse(request):
    logout(request)
    return redirect('taskspage')

# def LogoutResponse(request):
#     if request.session['user_id']:
#         del request.session['user_id']

#     return redirect('login')

def RegisterpageResponse(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, "password doesn't match")
        elif User.objects.filter(username=username).exists():
            messages.error(request,"username already exist")
        else:
            user = User.objects.create_user(username=username, password=pass1)
            login(request, user)
            return redirect('taskspage')
        
    return render(request,'register.html')



@login_required(login_url='login')
def TaskListResponse(request):
    # tasks = Tasks.objects.all()

    tasks = Tasks.objects.filter(user = request.user)
    count = tasks.filter(complete_status=False).count()

    search_value = request.GET.get('search') or ''
    if search_value:
        tasks = Tasks.objects.filter(title__contains=search_value)

    context={
        'task':tasks,
        'count':count, 
        'search_value':search_value
    }
    
    return render(request, 'tasks.html', context)

@login_required(login_url='login')
def TaskDetailResponse(request,id):
    task = Tasks.objects.get(id=id)
    return render(request,'task_details.html', context={'task':task})

@login_required(login_url='login')
def TaskCreateResponse(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        complete = request.POST.get('complete') == 'on'

        obj = Tasks()
        obj.user = request.user
        obj.title = title
        obj.desc = desc
        obj.complete_status = complete
        obj.save()

        return redirect('taskspage')
    
    return render(request, 'form.html', context={"user":request.user})

@login_required(login_url='login')
def TaskUpdateResponse(request, id):
    obj = Tasks.objects.get(id=id)

    if request.method == 'POST':
        if obj.user == request.user:
            title = request.POST['title']
            desc = request.POST['desc']
            complete = request.POST.get('complete') == 'on'

            obj.user = request.user
            obj.title = title
            obj.desc = desc
            obj.complete_status = complete
            obj.save()

            return redirect('taskspage')
        else:
            return HttpResponse('<h1>This is not belong to you</h1>')
    
    return render(request, 'filled_form.html', context={'task':obj})

@login_required(login_url='login')
def TaskDeleteResponse(request, id):
    task = Tasks.objects.get(id=id)

    if request.method == 'POST':
        if task.user == request.user:
            task.delete()
            return redirect('taskspage')
        else:
            return HttpResponse('<h1>This is not belong to you</h1>')
    
    return render(request, 'delete_confirm.html', context={'task':task})

