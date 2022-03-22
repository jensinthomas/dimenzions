from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def registeredusers(request):
    use = User.objects.all()
    context = {'use': use}
    username = request.POST.get('username')
    if User.objects.filter(username=username).exists():
        use = User.objects.filter(username=username)
    return render(request, 'registeredusers.html', context)
