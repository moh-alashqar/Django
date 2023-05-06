from django.urls import path
from . import views
urlpatterns = [
    path('', views.render_add_show_courses),
    path('add_show_courses', views.add_show_courses),
    path('courses/destroy/<int:id>', views.render_destroy_course),
    path('courses/destroy/<int:id>/confirm', views.confirm_destroy_course),
]