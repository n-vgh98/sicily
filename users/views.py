from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


def owner_dashboard(request):
    return render(request, 'users/owner/owner_base.html')


def owner_profile(request):
    return render(request, 'users/owner/show_profile.html')


def user_login(request):
    if request.user.is_anonymous:
        if request.method == 'GET':
            return render(request, 'users/authentication/authentication.html')
        elif request.method == 'POST':
            phone_number = request.POST['phone_number']
            password = request.POST['password']

            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('owner_profile')
            return redirect('user_login')
    return redirect('user_login')
