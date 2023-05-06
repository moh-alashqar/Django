from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_survey),
    path('/new', views.new_survey),
]