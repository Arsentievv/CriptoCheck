from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class CriptoModel(models.Model):

    """Модель валюты."""

    name = models.CharField(max_length=20, verbose_name='Name')
    symbol = models.CharField(max_length=10, verbose_name='Symbol')
    price = models.FloatField(default=0, verbose_name='Price')
    percent_change_24h = models.FloatField(default=0, verbose_name='Price change for 24 hours')
    volume_24h = models.FloatField(default=0, verbose_name='Selling volume for 24 hours')
    volume_change_24h = models.FloatField(default=0, verbose_name='Selling volume change for 24 hours')
    slug = models.SlugField(default=None, max_length=10, unique=True, db_index=True, verbose_name='URL')




class FavouriteCripto(models.Model):

    """Модель избранной валюты, связанная с моделями CriptoModel и User связью 1 ко многим."""

    cripto = models.ForeignKey(
        CriptoModel, null=True, default=None, on_delete=models.CASCADE, related_name='fave_cripto')
    user = models.ForeignKey(
        User, null=True, default=None, on_delete=models.CASCADE, related_name='fave_cripto_user')