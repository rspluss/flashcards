from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.


def index_profile(request):

    context = {}
    return render(request, "profiles/index.html", context)
