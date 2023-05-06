from django.db import models
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    rel_date = models.DateField()
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

def create_show(title, network, rel_date, desc):
    Show.objects.create(title=title, network=network, rel_date=rel_date, desc=desc)

def update_show(id, title, network, rel_date, desc):
    show = Show.objects.get(id=id)
    show.title = title
    show.network = network
    show.rel_date = rel_date
    show.desc = desc
    show.save()

def delete_show(id):
    show = Show.objects.get(id=id)
    show.delete()

def get_show(id):
    return Show.objects.get(id=id)

def get_all_shows():
    return Show.objects.all()

def get_last_show():
    return Show.objects.last()