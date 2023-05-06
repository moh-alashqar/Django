from django.shortcuts import render, redirect
from . import models

def render_add_show_courses(request):
    context = {
        'courses': models.get_all_courses(),
    }
    return render(request, 'add_show_courses.html', context)

def add_show_courses(request):
    course = request.POST
    models.create_course(name=course['name'], desc=course['desc'])
    return redirect('/')

def render_destroy_course(request, id):
    context = {
        'course': models.get_course(id),
    }
    return render(request, 'destroy_course.html', context)

def confirm_destroy_course(request, id):
    action = request.POST['submit']
    if action == 'Yes! I want to delete this':
        models.destroy_course(id)
    return redirect('/')
