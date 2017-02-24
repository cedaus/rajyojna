from django.shortcuts import render

# Create your views here.
def req_citizen_profile(request):
    print("rendering citzen profile template")


def req_citizen_login(request):
    data = {}
    return render(request, 'citizen_login.html', data)
