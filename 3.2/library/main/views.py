from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ViewSet, ModelViewSet
from django.shortcuts import render

from main.models import Book, Order
from main.serializers import BookSerializer


@api_view(['GET', 'POST'])
def books_list(request):
    """получите список книг из БД
    отсериализуйте и верните ответ
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request):
        # получите данные из запроса
        serializer = BookSerializer(...) #передайте данные из запроса в сериализатор
        if serializer.is_valid(raise_exception=True): #если данные валидны
            return Response('Книга успешно создана') # возвращаем ответ об этом


class BookDetailsView(RetrieveAPIView):
    # реализуйте логику получения деталей одного объявления
    queryset = Book.objects.all()
    serializer_class = BookSerializer()
    return Response(queryset)


class BookUpdateView(UpdateAPIView):
    # реализуйте логику обновления объявления
    ...


class BookDeleteView(DestroyAPIView):
    # реализуйте логику удаления объявления
    ...


class OrderViewSet(viewsets.ModelViewSet):
    # реализуйте CRUD для заказов
    ...
