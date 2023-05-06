from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('add_book', views.add_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('assign_book_author', views.assign_book_author),
    path('books/<int:id>', views.show_book),
    path('authors/<int:id>', views.show_author),
]