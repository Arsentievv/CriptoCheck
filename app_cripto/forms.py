from django import forms


class AddFaveCoinForm(forms.Form):

    """Форма добавления валюты в избранные, с невидимым полем id."""

    coin_id = forms.IntegerField(required=False, widget=forms.HiddenInput)