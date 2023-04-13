from django.shortcuts import render


def main(request, name=None):
    context = {"name": name}
    return render(request, 'menu/main.html', context)
