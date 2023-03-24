
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import (
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api_cripto.serializers import CriptoSerializer
from app_cripto.models import CriptoModel


class ResultsSetPagination(PageNumberPagination):

    """Представление для настройки пагинации списковых страниц приложения api_cripto."""

    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 2


class CriptoListApi(ListCreateAPIView):

    """Представление для получения списка валют, а также его создания."""

    queryset = CriptoModel.objects.all()
    serializer_class = CriptoSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):

        """Метод фильтрации списка валют по имени автора."""

        queryset = CriptoModel.objects.all()
        cripto_name = self.request.query_params.get('name')
        if cripto_name:
            queryset = queryset.filter(symbol=cripto_name)
        return queryset


class CriptoDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):

    """Представление для получения детальной информации о валюте, а также ее редактирование и удаление."""

    queryset = CriptoModel.objects.all()
    serializer_class = CriptoSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):

        """Метод получения детальной информации о валюте."""

        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):

        """Метод обоновления информации о валюте."""

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):

        """Метод удаления записи о валюте."""

        return self.destroy(request, *args, **kwargs)


