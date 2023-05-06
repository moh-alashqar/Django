from django.db import models
from datetime import date, datetime

class ShowManager(models.Manager):
    errors = {}
    def basic_validator(self, postData):
        self.errors = {}
        if len(postData['title']) < 2:
            self.set_error("title", "Title must be at least 2 characters!")
        if len(postData['network']) < 3:
            self.set_error("network", "Network must be at least 3 characters!")
        if len(postData['desc']) < 10 and len(postData['desc']) > 0:
            self.set_error("desc", "Descriptions must be at least 10 characters!")
        if len(postData['rel_date']) < 1:
            self.set_error("rel_date_blank", "Release date can't be blank!")
        else: 
            print(postData['rel_date'])
            print(date.today())
            if postData['rel_date'] > date.today().strftime("%Y-%m-%d"):
                self.set_error("rel_date_old", "Release date can't be in the future!")
        print(len(self.errors))
        return self.errors

    def create_validator(self, postData):
        shows = get_all_shows()
        for show in shows:
            if postData['title'] == show.title:
                self.set_error("title", "Show already exists!")
                break
        return self.errors

# filter show by name __ filter __ if there is data : exists __ if no create

    def set_error(self, key, msg):
        self.errors[key] = msg

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    rel_date = models.DateField()
    desc = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

def validate_create(postData):
    Show.objects.basic_validator(postData)
    return Show.objects.create_validator(postData)

def validate_update(postData):
    return Show.objects.basic_validator(postData)

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