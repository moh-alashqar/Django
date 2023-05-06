from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name="authors")

def create_book(title, desc):
    try:
        Book.objects.create(title=title, desc=desc)
        return True
    except KeyError:
        return False

def create_author(first_name, last_name, notes):
    try:
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return True
    except KeyError:
        return False

def assign_book_author(book_id, author_id):
    try:
        get_author(author_id).books.add(get_book(book_id))
        return True
    except KeyError:
        return False

def get_book(book_id):
    return Book.objects.get(id=book_id)

def get_author(author_id):
    return Author.objects.get(id=author_id)

def get_all_books():
    return Book.objects.all()

def get_all_authors():
    return Author.objects.all()

def get_author_books(author_id):
    author = get_author(author_id)
    return author.books.all()

def get_book_authors(book_id):
    book = get_book(book_id)
    return book.authors.all()

def get_unassigned_books():
    books = get_all_books()
    unassigned_books = []
    for book in books:
        if len(get_book_authors(book.id)) < 1:
            unassigned_books.append(book)
    return unassigned_books

def get_unassigned_authors():
    authors = get_all_authors()
    unassigned_authors = []
    for author in authors:
        if len(get_author_books(author.id)) < 1:
            unassigned_authors.append(author)
    return unassigned_authors

    # leet codes

# login resig
# tv shows 