from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('process', views.process),
    path('end', views.end),
]