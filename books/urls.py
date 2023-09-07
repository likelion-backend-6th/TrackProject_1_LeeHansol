from django.urls import path
from books import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('my_rentals/', views.ManageBookListView.as_view(), name='manage_book_list'),
    # path('books/<book_id>/', views.BookDetailView.as_view(), name='book_detail'),
    ]