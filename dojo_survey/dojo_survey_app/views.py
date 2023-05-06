from django.shortcuts import render, redirect

def signup(request):
    return render(request, 'signup.html')

def result(request):
    if request.method == 'POST':
        try:
            ninja = "Yes" if request.POST['ninja'] == "on" else "No"
        except:
            ninja = "No"
        try: 
            m_status = request.POST['m_status']
        except:
            m_status = "None"
        context = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'lang': request.POST['lang'],
            'm_status': m_status,
            'ninja': ninja,
            'comment': request.POST['comment']
        }
        return render(request, 'result.html', context)
    else: 
        return redirect('/')
