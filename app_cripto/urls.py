from django.urls import path
from .views import (
    MainPaigeView,
    CriptoListView,
    SearchResultView,
    FaveCoinsList,
    CriptoNews


)


urlpatterns = [
    path('main_paige/', MainPaigeView.as_view(), name='main_paige'),
    path('cripto_list/', CriptoListView.as_view(), name='cripto_list'),
    path('search_results/', SearchResultView.as_view(), name='search_results'),
    path('fave_coins/', FaveCoinsList.as_view(), name='fave_coins'),
    path('cripto_news/', CriptoNews.as_view(), name='cripto_news')
]