from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def root(request):
    return redirect('/blogs')
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")
def create(request):
    return redirect('/')
def show(request, number):
    context = {
        'string': "Placeholder to display blog number:",
        'number': number
    }
    return render(request, "show.html", context)
def edit(request, number):
    context = {
        'string': "Placeholder to edit blog",
        'number': number
    }
    return render(request, "show.html", context)
def destroy(request, number):
    return redirect('/blogs')
def json(request):
    return JsonResponse({"response": "JSON response from json method", "status": True})

