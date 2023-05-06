from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_current_time),
    path('time_display', views.show_current_time),
]