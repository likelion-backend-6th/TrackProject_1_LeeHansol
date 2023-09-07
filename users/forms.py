from django import forms
from books.models import Item


class BookRentalForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all(), widget=forms.HiddenInput)