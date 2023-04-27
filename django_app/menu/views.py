from django.shortcuts import render


def Menu(request, item=None):
    return render(request, 'index.html', {'item': item})
