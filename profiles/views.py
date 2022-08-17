from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from flashcard.models import FlashCard, Category
from flashcard.forms import AddCardForm

# Create your views here.


def index_profile(request):
    cards = FlashCard.objects.all()
    categories = Category.objects.all()

    context = {"cards": cards, "categories": categories}
    return render(request, "profiles/index.html", context)


def categories(request, pk):
    category = Category.objects.get(id=pk)

    context = {"category": category}
    return render(request, "flashcard/cards.html", context)


def add_card(request):
    if request.method == 'POST':
        add_card_form = AddCardForm(request.POST)
        if add_card_form.is_valid():
            add_card_form.save()
        return redirect("profiles:index_profile")
    else:
        add_card_form = AddCardForm()

    context = {"add_card_form": add_card_form}
    return render(request, "profiles/add_card.html", context)


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profiles:index_profile')
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/register_user.html", context)