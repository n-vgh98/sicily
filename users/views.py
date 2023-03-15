from django.shortcuts import render

def owner_dashboard(request):
    return render(request, 'users/owner/owner_dashboard.html')
