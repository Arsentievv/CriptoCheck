import requests
import json
from newsapi import NewsApiClient
from django import views

from django.db.models import Q
from django.http import HttpResponseRedirect

from app_cripto.forms import AddFaveCoinForm
from cripto_project.settings import API_KEY, NEWS_API_KEY
from django.shortcuts import render, redirect
from django.views import generic
from app_cripto.models import CriptoModel, FavouriteCripto


class MainPaigeView(generic.TemplateView):

    """Представление главной страницы."""

    template_name = 'app_cripto/main_paige.html'


class CriptoListView(generic.ListView):

    """Представление списка валют."""

    model = CriptoModel
    template_name = 'app_cripto/cripto_list.html'
    context_object_name = 'cripto_list'

    def get_context_data(self, **kwargs):

        """Метод передавания формы добавления валюты в избранное."""

        context = super().get_context_data(**kwargs)
        context['form'] = AddFaveCoinForm
        return context

    def get(self, request, *args, **kwargs):

        """
        Метод отображения списка валют из API.
        В шаблон передается вся информация о валюте и кнопка добавления
        валюты в избранное.
        """

        params = {
            'start': '1',
            'limit': None,
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY,
        }
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        json_result = requests.get(url, params=params, headers=headers).json()
        coins = json_result['data']
        for coin in coins:
            CriptoModel.objects.get_or_create(
                name=coin['name'], symbol=coin['symbol'], slug=coin['symbol'],
                )
            cert_coin = CriptoModel.objects.get(name=coin['name'])
            cert_coin.price = coin['quote']['USD']['price']
            cert_coin.percent_change_24h = coin['quote']['USD']['percent_change_24h']
            cert_coin.volume_24h = coin['quote']['USD']['volume_24h']
            cert_coin.volume_change_24h = coin['quote']['USD']['volume_change_24h']
            cert_coin.save()
        cripto_list = CriptoModel.objects.all()
        return render(request, 'app_cripto/cripto_list.html', context={'cripto_list': cripto_list})

    def post(self, request, **kwargs):

        """Метод добавления валюты в избранное."""

        form = AddFaveCoinForm(request.POST)
        coin = CriptoModel.objects.get(id=request.POST.get('coin_id'))
        if form.is_valid():
            fave = FavouriteCripto.objects.create(cripto=coin, user=request.user)
            fave.save()
            return HttpResponseRedirect('/cripto/cripto_list/')
        return redirect('/cripto/cripto_list/')


class SearchResultView(generic.ListView):

    """Представление для поиска валют по коду или названию."""

    model = CriptoModel
    template_name = 'app_cripto/search_result.html'

    def get_queryset(self):

        """
        Метод получения искомой пользователем валюты из БД и передачи
        в шаблон.
        """

        query = self.request.GET.get('q')
        object_list = CriptoModel.objects.filter(
            Q(name__icontains=query) | Q(symbol__icontains=query)
        )
        return object_list


class FaveCoinsList(generic.ListView):

    """Представление списка избранных валют."""

    template_name = 'app_cripto/fave_coins.html'
    model = FavouriteCripto
    context_object_name = 'fave_coins'

    def get_context_data(self, *args, **kwargs):

        """
        Метод передачи в шаблон отсортированного по полю User списка валют
        из модели избранных валют.
        """

        context = super().get_context_data(**kwargs)
        context['fave_coins'] = FavouriteCripto.objects.filter(user=self.request.user)
        return context

class CriptoNews(views.View):

    """Представление получения новостей о крипто-валюте из API."""

    def get(self, request):

        """Метод получения новостей."""

        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        all_articles = newsapi.get_everything(q='bitcoin',
                                              language='en',
                                              sort_by='relevancy',
                                              )
        return render(request, 'app_cripto/cripto_news.html', context={
            'all_articles': all_articles
        })

