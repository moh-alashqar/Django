from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if not 'points' in request.session:
        request.session['points'] = 0
        request.session['logs'] = []
    return render(request, 'index.html')

def process_money(request):
    print(request.POST['which_section'])
    match request.POST['which_section']:
        case 'Farm':
            set_points(request, 10, 20)
        case 'Cave':
            set_points(request, 10, 20)
        case 'House':
            set_points(request, 10, 20)
        case 'Quest':
            set_points(request, -50, 50)
        case _:
            pass
    return redirect('/')

def start_again(request):
    request.session.flush()
    return redirect('/')

def set_points(request, min, max):
    randInt = get_randInt(min, max)
    print(randInt)
    request.session['points'] += randInt
    set_status(request, randInt)

def get_randInt(min, max):
    return random.randint(min, max)

def set_status(request, randInt):
    dateTime = get_date_time()
    if randInt <= 0: 
        color = "red"
        status = f"You failed a quest and lost {randInt} gold. Ouch. ({dateTime})"
    else:
        color = "green"
        if request.POST['which_section'] == 'Quest':
            status = f"You completed the quest and earned {randInt} gold. ({dateTime})"
        else:
            status = f"You entered a {request.POST['which_section']} and earned {randInt} gold. ({dateTime})"
    request.session['logs'].append((color, status))

def get_date_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
