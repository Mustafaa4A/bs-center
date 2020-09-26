from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def myaccount(request):
    return render(request, 'myaccount.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Incorect username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if first_name.isalpha() and last_name.isalpha():
            if len(str(password1)) >= 8:
                if password1 == password2:
                    if User.objects.filter(username=username):
                        messages.error(request, 'Username already taken')
                        return redirect('register')
                    elif User.objects.filter(email=email):
                        messages.error(request, 'Email already taken')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(username=username, first_name=first_name,
                                                        last_name=last_name, email=email, password=password1)
                        user.save()
                        return redirect('login')
                else:
                    messages.error(request, 'Password not matching')
                    return redirect('register')
            else:
                messages.error(
                    request, 'Your password must contain at least 8 characters')
                return redirect('register')
            return redirect('/')
        else:
            messages.error(
                request, 'First name or last name can\'t contain numerics or symbols.')
            return redirect('register')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
