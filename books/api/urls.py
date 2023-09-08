from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'books'

router = routers.DefaultRouter()
router.register('books', views.ItemViewSet)

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='subject_list'),
    path('items/<pk>/', views.ItemDetailView.as_view(), name='subject_detail'),
    path('', include(router.urls)),
    ]