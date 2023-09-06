from django.urls import path
from books import views

urlpatterns = [
    path('my_rentals/', views.ManageBookListView.as_view(), name='manage_book_list'),
    ]