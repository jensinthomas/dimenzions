from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.


def registeredusers(request):
    use = User.objects.all()
    return render(request, 'registeredusers.html', {'use': use})


def delete(request, id):
    use = User.objects.get(id=id)
    use.delete()
    return redirect('registeredusers')
