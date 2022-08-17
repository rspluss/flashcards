from django import forms

from flashcard.models import FlashCard


class AddCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard
        fields = ['name_pl', 'name_eng', 'category']

        widget = {
            "name_pl": forms.TextInput(attrs={"class": "form-control"}),
            "name_eng": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.CheckboxInput(attrs={"class": "form-control"})
        }
