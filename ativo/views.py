from django.shortcuts import render


def index(request):


    context = {
    
    }
    return render(request, 'ativo/index.html', context)


def add(request):
    return render(request, 'ativo/add.html')
