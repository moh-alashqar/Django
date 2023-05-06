from django.db import models
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Name must be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Description must be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

def create_course(name, desc):
    Course.objects.create(name=name, desc=desc)

def get_course(id):
    return Course.objects.get(id=id)

def get_all_courses():
    return Course.objects.all()

def destroy_course(id):
    course = Course.objects.get(id=id)
    course.delete()
