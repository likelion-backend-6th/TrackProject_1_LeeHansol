from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from books.api.permissions import IsRental
from books.api.serializers import ItemSerializer
from books.models import Item
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BookRentalView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        book = get_object_or_404(Item, pk=pk)
        book.users.add(request.user)
        return Response({'enrolled': True})


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def rent(self, request, *args, **kwargs):
        item = self.get_object()
        item.users.add(request.user)
        return Response({'rent': True})

    @action(detail=True, methods=['get'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsRental])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)