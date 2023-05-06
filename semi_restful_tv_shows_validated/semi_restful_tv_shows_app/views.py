from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

def create_show(request):
    return render(request, 'create_show.html')

def update_book(request, id):
    show = models.get_show(id=id)
    rel_date_formatted = show.rel_date.strftime("%Y-%m-%d")
    print(rel_date_formatted)
    context = {
        'show': show,
        'rel_date': rel_date_formatted,
    }
    return render(request, 'update_show.html', context)

def process_create_show(request):
    show = request.POST
    errors = models.validate_create(show)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        models.create_show(title=show['title'], network=show['network'], rel_date=show['rel_date'], desc=show['desc'])
        id = models.get_last_show().id
        return redirect('/shows/'+str(id))

def process_update_show(request):
    show = request.POST
    id = show['id']
    errors = models.validate_update(show)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')
    else:
        models.update_show(id=show['id'], title=show['title'], network=show['network'], rel_date=show['rel_date'], desc=show['desc'])
        return redirect('/shows/'+str(id))

def show_book(request, id):
    context = {
        'show': models.get_show(id=id)
    }
    return render(request, 'info_show.html', context)

def all_shows(request):
    context = {
        'shows': models.get_all_shows()
    }
    return render(request, 'info_all_shows.html', context)

def delete_book(request, id):
    models.delete_show(id=id)
    return redirect('/shows')