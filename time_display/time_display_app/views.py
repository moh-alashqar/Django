from django.shortcuts import render
import os, time

def show_current_time(request):
    curr_time = time.localtime()
    context = {
        'time': time.strftime("%I:%M %p", curr_time),
        'date': time.strftime("%b %d, %Y", curr_time),
    }
    return render(request, "index.html", context)
