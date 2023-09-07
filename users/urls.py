from django.urls import path

from users import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user_registration'),
    path('books/<int:book_id>/rent/', views.UserBookRentalView.as_view(), name='user_book_rental'),
]