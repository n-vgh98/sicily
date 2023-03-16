from django.shortcuts import render, get_object_or_404
from .models import Coffeeshop, Game


def index(request):
    return render(request, 'coffeeshops/index.html')


def coffeeshops_list(request):
    coffeeshops = Coffeeshop.objects.all()
    context = {
        'coffeeshops': coffeeshops
    }
    return render(request, 'coffeeshops/coffeeshops_list.html', context=context)


def games_list(request, pk):
    coffeeshop = get_object_or_404(Coffeeshop, pk=pk)
    games = Game.objects.filter(coffeeshop__id=coffeeshop.id, status=True)
    context = {
        'coffeeshop': coffeeshop,
        'games': games,
    }
    return render(request, 'coffeeshops/games_list.html', context=context)
