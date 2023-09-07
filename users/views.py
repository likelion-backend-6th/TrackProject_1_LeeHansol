from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.forms import BookRentalForm


# Create your views here.

class UserRegistrationView(CreateView):
    template_name = 'users/user/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user_rental_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        login(self.request, user)
        return result


class UserBookRentalView(LoginRequiredMixin, FormView):
    item = None
    form_class = BookRentalForm

    def form_valid(self, form):
        self.item = form.cleaned_data['item']
        self.item.users.add(self.request.user)
        return super().form_valid(form)