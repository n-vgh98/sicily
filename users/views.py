from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from coffeeshops.models import Coffeeshop, Game


def owner_dashboard(request):
    return render(request, 'users/owner/owner_base.html')


def owner_profile(request):
    if request.method == 'GET':
        my_coffeeshops = Coffeeshop.objects.filter(owner=request.user.id)
        context = {
            'my_coffeeshops': my_coffeeshops,
        }
        return render(request, 'users/owner/show_profile.html', context=context)
    # elif request.method == 'POST':
    #     name = request.POST['name']
    #     address = request.POST['address']
    #     description = request.POST['description']
    #     main_image = request.POST['main_image']


def edit_owner_profile(request, pk):
    coffeeshop = get_object_or_404(Coffeeshop, pk=pk)
    coffeeshop.name = request.POST['name']
    coffeeshop.address = request.POST['address']
    coffeeshop.description = request.POST['description']
    coffeeshop.main_image = request.POST['main_image']
    coffeeshop.save()

    return redirect('owner_dashboard')


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


def owner_game(request):
    if request.method == 'GET':
        games = Game.objects.filter(coffeeshop__owner=request.user.id)
        context = {
            'games': games
        }
        return render(request, 'users/owner/show_game.html', context=context)
