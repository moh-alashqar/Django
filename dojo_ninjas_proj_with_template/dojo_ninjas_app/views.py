from django.shortcuts import render, redirect
from . import models

def main(request):
    context = {
        'dojos': models.get_all_dojos(),
    }
    return render(request, 'main.html', context)

def add_dojo(request):
    dojo = request.POST
    name = dojo['name']
    city = dojo['city']
    state = dojo['state']
    models.add_dojo(name, city, state)
    return redirect('/')

def add_ninja(request):
    ninja = request.POST
    first_name = ninja['first_name']
    last_name = ninja['last_name']
    dojo_id = ninja['dojo_id']
    models.add_ninja(first_name, last_name, dojo_id)
    return redirect('/')

def del_dojo(request):
    dojo_id = request.POST['dojo_id']
    models.del_dojo(dojo_id)
    return redirect('/')