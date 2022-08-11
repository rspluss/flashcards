from django.shortcuts import render


def index(request):

    context = {}
    return render(request, "home/index.html", context)


def shop(request):

    context = {}
    return render(request, "home/shop.html", context)


def profile(request):

    context = {}
    return render(request, "home/profile.html", context)


def price(request):

    context = {}
    return render(request, "home/price.html", context)
