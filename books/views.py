from django.views.generic import ListView, DetailView

from books.models import Item
from users.forms import BookRentalForm


class BookListView(ListView):
    def get(self, request):
        items = Item.objects.all()
        from django.shortcuts import render
        return render(request, 'books/book/list.html', {'items': items})


class ManageBookListView(ListView):
    template_name = 'books/manage/list.html'


# class BookDetailView(DetailView):
#     model = Item
#     template_name = 'books/book/detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rental_form'] = BookRentalForm(initial={'item': self.object})
#         return context
