from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from flashcard.models import FlashCard, Category, Card
from flashcard.forms import AddCardForm, CardAddForm
from django.contrib import messages
from flashcard.forms import CardCheckForm
import random
from django.views.generic import ListView



def index_profile(request):
    cards = FlashCard.objects.all()
    categories = Category.objects.all()
    cards_f = Card.objects.all().order_by("box", "-date_created")

    context = {"cards": cards, "categories": categories, "cards_f": cards_f}
    return render(request, "profiles/index.html", context)


def categories(request, pk):
    category = Category.objects.get(id=pk)

    context = {"category": category}
    return render(request, "flashcard/cards.html", context)


def add_card(request):
    if request.method == 'POST':
        add_card_f_form = CardAddForm(request.POST)
        if add_card_f_form.is_valid():
            add_card_f_form.save()
            messages.success(request, "Fiszka została dodana poprawnie!")
            return redirect("profiles:index_profile")
    else:
        add_card_f_form = CardAddForm()

    context = {"add_card_f_form": add_card_f_form}
    return render(request, "profiles/add_card.html", context)


def edit_card(request, pk):
    card = Card.objects.get(pk=pk)
    if request.method == 'POST':
        form = CardAddForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, "Fiszka została edytowana")
            return redirect("profiles:index_profile")
    else:
        form = CardAddForm(instance=card)
    context = {"form": form}
    return render(request, "profiles/edit_card.html", context)


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
    edit_user = UserChangeForm()
    if request.method == 'POST':
        if "edit_user" in request.POST:
            form = UserChangeForm(data=request.POST, instance=edit_user)
            if form.is_valid():
                form.save()
                username = edit_user.cleaned_data['username']
                email = edit_user.cleaned_data['email']
                password = edit_user.cleaned_data['password1']
                user = authenticate(username=username, password=password, email=email)
    else:
        edit_user = UserChangeForm()

    context = {"edit_user": edit_user}
    return render(request, "registration/edit_profile.html", context)


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")


class BoxView(CardListView):
    template_name = "flashcard/include/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])
        return redirect(request.META.get("HTTP_REFERER"))