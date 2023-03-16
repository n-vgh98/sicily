from django.shortcuts import render
from .models import Coffeeshop

def index(request):
    return render(request, 'coffeeshops/index.html')


def coffeeshops_list(request):
    coffeeshops = Coffeeshop.objects.all()
    context = {
        'coffeeshops':coffeeshops
    }
    return render(request, 'coffeeshops/coffeeshops_list.html', context=context)
