from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from coffeeshops.models import Coffeeshop


def owner_dashboard(request):
    return render(request, 'users/owner/owner_base.html')


def owner_profile(request):
    if request.method == 'GET':
        my_coffeeshops = Coffeeshop.objects.filter(owner=request.user.id)
        context = {
            'my_coffeeshops': my_coffeeshops,
        }
        return render(request, 'users/owner/show_profile.html', context=context)


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
                owner = Coffeeshop.objects.filter(owner=user.id)
                if owner:
                    return redirect('owner_profile')
                return HttpResponse('you are user')  # TODO return to home
            return HttpResponse('you are not user')  # TODO create MESSAGE
    return HttpResponse('you are annoymous')  # TODO CREATE MESSAGE


def user_logout(request):
    logout(request)
    return redirect('user_login')


class SignUp(CreateView):
    form_class = CustomUserForm
    template_name = 'users/authentication/sign_up.html'
    success_url = reverse_lazy('user_login')
