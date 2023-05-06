from django.shortcuts import render, redirect
import random

def main(request):
    if not 'random' in request.session:
        init(request)
    return render(request, 'result.html')

def process(request):
    guess = request.POST['guess']
    request.session['attempts'] += 1
    check_guess(request, guess)
    return redirect('/')

def check_guess(request, guess):
    try: 
        guess = int(guess)
        random = request.session['random']
        sub = guess - random
        if guess > 100 or guess < 0:
            invalid_input(request)
        elif sub > 0:
            wrong_attempt(request)
            request.session['status'] = 'Too High!'
        elif sub == 0:
            right_attempt(request, guess)
        else:
            wrong_attempt(request)
            request.session['status'] = 'Too Low!'
    except ValueError:
        invalid_input(request)
    is_done(request)

def invalid_input(request):
    request.session['status'] = 'Invalid input!'
    request.session['colo'] = 'red'

def wrong_attempt(request):
    request.session['colo'] = 'red'

def right_attempt(request, guess):
    request.session['colo'] = 'green'
    won_msg = str(guess) + " was the number!"
    request.session['status'] = won_msg
    request.session['won'] = True

def end(request):
    clear_session(request)
    return redirect('/')

def is_done(request):
    if request.session['attempts'] >= 5 or request.session['won']:
        request.session['done'] = True
        return True
    else: 
        return False

def init(request):
    request.session['random'] = random.randint(1, 100)
    print(request.session['random'])
    request.session['attempts'] = 0
    request.session['done'] = False
    request.session['won'] = False

def clear_session(request):
    request.session.flush()