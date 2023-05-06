from django.shortcuts import render, redirect
from . import models

def books(request):
    context = {
        'books': models.get_all_books,
    }
    return render(request, 'books.html', context)

def add_book(request):
    book = request.POST
    title = book['title']
    desc = book['desc']
    models.create_book(title=title, desc=desc)
    return redirect('/')

def show_book(request, id):
    context = {
        'book': models.get_book(id),
        'unauthors': models.get_unassigned_authors(),
    }
    return render(request, 'show_book.html', context)

def authors(request):
    context = {
        'authors': models.get_all_authors,
    }
    return render(request, 'authors.html', context)

def add_author(request):
    author = request.POST
    first_name = author['first_name']
    last_name = author['last_name']
    notes = author['notes']
    models.create_author(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

def show_author(request, id):
    context = {
        'author': models.get_author(id),
        'unbooks': models.get_unassigned_books(),
    }
    return render(request, 'show_author.html', context)

def assign_book_author(request):
    post = request.POST
    book_id = post['book_id']
    author_id = post['author_id']
    models.assign_book_author(book_id, author_id)
    form = post['which_temp']
    return redirect(form)