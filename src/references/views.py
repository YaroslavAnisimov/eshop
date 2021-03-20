from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.db.models import Q
from . import forms

from references.models import Book

# (UserPassesTestMixin, ListView) 

class BooksList (LoginRequiredMixin, ListView) :
   model = Book
   login_url = '/admin/login/'
   paginate_by = 10  #elements per page

   def get_ordering(self):
      ordering_by = "pk"
      field_to_sort_on = self.request.GET.get('field')
      direction_to_sort_on = self.request.GET.get ('direction')
      if field_to_sort_on and direction_to_sort_on:
         direction = {'up': ""}
         ordering_by = f'{direction.get(direction_to_sort_on,"-")}{field_to_sort_on}'
      return ordering_by 
      #    if direction_to_sort_on == 'up':
      #       direction = ""
      #    else:
      #       direction = "-" 

   def get_queryset(self):
      guery = self.request.GET.get('query')
      print(query)
      qs = super().get_queryset()
      if query:
         qs = qs.filter(Q(description_contains=query)|Q(name_contains=query) )
      return qs

   def get_context_data (self, **kwargs):
      context = super().get_context_data (**kwargs)
      context ['page_title'] = "Books"
      field_to_sort_on = self.request.GET.get('field')
      direction_to_sort_on = self.request.GET.get ('direction')
      query = self.request.GET.get('query')
      context ['search_form'] = forms.SearchForm(
         initial={
            'query':query,
            'field':field_to_sort_on,
            'direction': direction_to_sort_on,
         })
      context ['field_to_sort_on'] = field_to_sort_on
      context ['direction_to_sort_on'] = direction_to_sort_on
      return context

#    def test_func (self):
        # first_name = self.request.user.first_name 
        # pk = self.request.user.pk
        # return f"{pk}" == "1"

class BookDetail (DetailView):
   model = Book
#    queryset = Book.objects.all() - work too

class BookDelete (DeleteView):
   success_url = reverse_lazy ('books-list')
   model =  Book



class BookCreate (CreateView):
   model = Book
#    fields = ('book_name', 'book_description')
   success_url = reverse_lazy ('books-list')
   form_class = forms.BookForm

class BookUpdate (UpdateView):
   model = Book
   success_url ='/books-list/'
#  form_class = forms.BookUpdate (needs to add form in forms.py)
   fields = ('book_name', 'authors', 'book_description')







# def book_update (request):
#     context= {}
#     if request.metod == 'GET':
#         book = Book.objects.get (pk =pk)
#         context = {'name': book.name, 'description': book.description}
#     elif request.method == 'POST':
#         name = request.POST.get ('name')
#         description = request.POST.get ('description')
#         book = Book.objects.get (pk = pk)
#         book.name = name 
#         book.description = description
#         book.save()
#         return HttpResponseRedirect (reverse ('book-detail', kwargs = {'pk': book.pk }))
#     return render(request, template_name="update.html", context= context)


# def books_list (request):
#     books = Author.objects.all()
#     context= {"books": books}
#     return render(request, template_name="home.html", context= context)

# def book_detail (request, pk):
#     book = Book.objects.get (pk = pk)
#     context= {"object": book}
#     return render(request, template_name="detail.html", context= context)

# def book_delete (request, pk):
#     book = Book.objects.get (pk = pk)
#     authors = author.authors.all()
#     authors_count = authors.count() 
#     message = f'Book {book.name} with {authors_count} reviews has just been deleted !' #name = book_name(?)
#     authors.delete()
#     book.delete () 
#     context= {"message": message}
#     return render(request, template_name="delete.html", context = context)

# def book_create(request):
#     if request.method == 'POST':
#         name = request.POST.get ('name')
#         description= request.POST.get ('description')
#         book = Book.objects.create (name = name , description = description)
#         return HttpResponseRedirect (reverse('author-detail', kwargs = {'pk':author.pk}))
#     context = {'form': forms.BookForm()}
#     return render (request, template_name = "create.html", context = context)


# def book_create (request):
#     context = {}
#     if request.method == 'POST':
#        form = forms.BookForm(request.POST)
#        if form.is_valid():
#            book = form.save() 
#            return HttpResponseRedirect (reverse ('book-detail', kwargs = {'pk': book.pk }))
#        else:
#            context['form'] = form
#     else:
#        context['form'] = forms.BookForm()
#     return render(request, template_name="create.html", context= context)




