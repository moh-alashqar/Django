from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)

def get_all_dojos():
    return Dojo.objects.all()

def add_dojo(name, city, state):
    try:
        Dojo.objects.create(name=name, city=city, state=state)
        return True
    except KeyError:
        return False

def add_ninja(first_name, last_name, dojo_id):
    try:
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
        return True
    except KeyError:
        return False

def del_dojo(dojo_id):
    try:
        dojo = Dojo.objects.get(id=dojo_id)
        dojo.delete()
        return True
    except KeyError:
        return False