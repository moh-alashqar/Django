from django.shortcuts import render, redirect
from . import models

def create_show(request):
    context = {
        'which_form': 'create',
    }
    return render(request, 'add_edit_show.html', context)

def process_show(request):
    show = request.POST
    which_form = show['which_form']
    if which_form == 'create':
        models.create_show(title=show['title'], network=show['network'], rel_date=show['rel_date'], desc=show['desc'])
        id = models.get_last_show().id
    elif which_form == 'update':
        models.update_show(id=show['id'], title=show['title'], network=show['network'], rel_date=show['rel_date'], desc=show['desc'])
        id = show['id']
    return redirect('/shows/'+str(id))

def all_shows(request):
    context = {
        'shows': models.get_all_shows()
    }
    return render(request, 'info_all_shows.html', context)

def show_book(request, id):
    context = {
        'show': models.get_show(id=id)
    }
    return render(request, 'info_show.html', context)

def edit_book(request, id):
    show = models.get_show(id=id)
    rel_date_formatted = show.rel_date.strftime("%Y-%m-%d")
    print(rel_date_formatted)
    context = {
        'which_form': 'update',
        'show': show,
        'rel_date': rel_date_formatted,
    }
    return render(request, 'add_edit_show.html', context)

def delete_book(request, id):
    models.delete_show(id=id)
    return redirect('/shows')