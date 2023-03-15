from django.shortcuts import render


def owner_dashboard(request):
    return render(request, 'users/owner/owner_base.html')


def owner_profile(request):
    return render(request, 'users/owner/show_profile.html')


def login(request):
    return render(request, 'users/authentication/authentication.html')
