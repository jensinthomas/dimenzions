from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.


def registeredusers(request):
    use = Admin_register.objects.all()
    return render(request, 'registeredusers.html', {'use': use})


def delete(request, reg_id):
    use = Admin_register.objects.get(reg_id=reg_id)
    use.delete()
    return redirect('registeredusers')
