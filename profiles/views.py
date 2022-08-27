from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from flashcard.models import FlashCard, Category
from flashcard.forms import AddCardForm
from django.contrib import messages
from flashcard.forms import CardCheckForm


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
        messages.success(request, "Fiszka została dodana poprawnie!")
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
            messages.success(request, "Zostałeś poprawnie zarejestrowany!")
            return redirect('profiles:index_profile')
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/register_user.html", context)


def edit_profile(request):
    if request.method == 'POST':
        if "edit_user" in request.POST:
            edit_user = UserChangeForm(request.POST)
            if edit_user.is_valid():
                edit_user.save()
                username = edit_user.cleaned_data['username']
                email = edit_user.cleaned_data['email']
                password = edit_user.cleaned_data['password1']
                user = authenticate(username=username, password=password, email=email)
    else:
        edit_user = UserChangeForm()

    context = {"edit_user": edit_user}
    return render(request, "registration/edit_profile.html", context)
