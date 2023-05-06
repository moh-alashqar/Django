from django.shortcuts import render, HttpResponse
def show_survey(request):
    return HttpResponse("Placeholder to display all the surveys created")

def new_survey(request):
    return HttpResponse("Placeholder for users to add a new survey")