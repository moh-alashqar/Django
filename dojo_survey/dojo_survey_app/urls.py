from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup),
    path('result', views.result),
]