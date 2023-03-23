from django.urls import path


from api_cripto.views import CriptoListApi, CriptoDetail

urlpatterns = [
    path('cripto_list_api/', CriptoListApi.as_view(), name='cripto_list_api'),
    path('cripto_list_api/<int:pk>', CriptoDetail.as_view(), name='cripto_detail'),
]

