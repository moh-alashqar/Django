from django.urls import path
from django.shortcuts import redirect
from . import views
urlpatterns = [
    path('', lambda request: redirect('/shows', permanent=False)),
    path('shows/new', views.create_show),
    path('process_create_show', views.process_create_show),
    path('process_update_show', views.process_update_show),
    path('shows', views.all_shows),
    path('shows/<int:id>', views.show_book),
    path('shows/<int:id>/edit', views.update_book),
    path('shows/<int:id>/destroy', views.delete_book),
]