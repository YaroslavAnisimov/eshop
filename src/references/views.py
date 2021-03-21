from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from references import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
# Dictionaries ListViews
class AuthorsList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_authors'
    model = models.Authors
    template_name = 'references/list_authors.html'
    

class GenresList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_genres'
    model = models.Genres
    template_name = 'references/list_genres.html'
    

class SeriesList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_series'
    model = models.Series
    template_name = 'references/list_series.html'


class PublishersList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_publishers'
    model = models.Publishers
    template_name = 'references/list_publishers.html'


class AgeCategoriesList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_agecategories'
    model = models.AgeCategories
    template_name = 'references/list_age_categories.html'


# class BookFormatsList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
#     paginate_by = 10
#     login_url = reverse_lazy('login')
#     permission_required = 'references.view_bookformats'
#     model = models.BookFormats
#     template_name = 'references/list_book_formats.html'


# references generic.DeleteViews
class AuthorsDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_authors'
    model = models.Authors
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class GenresDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_genres'
    model = models.Genres
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('genres-list')


class SeriesDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_series'
    model = models.Series
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('series-list')


class PublishersDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_publishers'
    model = models.Publishers
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_agecategories'
    model = models.AgeCategories
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('age_categories-list')


# class BookFormatsDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
#     login_url = reverse_lazy('login')
#     permission_required = 'references.delete_bookformats'
#     model = models.BookFormats
#     template_name = 'references/form_confirm_delete.html'
#     success_url = reverse_lazy('boo_formats-list')


# references UpdateViews
class AuthorsUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_authors'
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_genres'
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_publishers'
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_agecategories'
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


# class BookFormatsUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
#     login_url = reverse_lazy('login')
#     permission_required = 'references.change_bookformats'
#     model = models.BookFormats
#     form_class = forms.BookFormatsForm
#     template_name = 'references/form_create_update.html'
#     success_url = reverse_lazy('book_formats-list')


# references CreateViews
class AuthorsCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_authors'
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_genres'
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_publishers'
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_agecategories'
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


# class BookFormatsCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
#     login_url = reverse_lazy('login')
#     permission_required = 'references.add_bookformats'
#     model = models.BookFormats
#     form_class = forms.BookFormatsForm
#     template_name = 'references/form_create_update.html'
#     success_url = reverse_lazy('book_formats-list')






# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse, reverse_lazy 
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
# from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
# from django.db.models import Q
# from . import forms

# from references.models import Book

# # (UserPassesTestMixin, ListView) 

# class BooksList (LoginRequiredMixin, ListView) :
#    model = Book
#    login_url = '/admin/login/'
#    paginate_by = 10  #elements per page

#    def get_ordering(self):
#       ordering_by = "pk"
#       field_to_sort_on = self.request.GET.get('field')
#       direction_to_sort_on = self.request.GET.get ('direction')
#       if field_to_sort_on and direction_to_sort_on:
#          direction = {'up': ""}
#          ordering_by = f'{direction.get(direction_to_sort_on,"-")}{field_to_sort_on}'
#       return ordering_by
   
#       #    if direction_to_sort_on == 'up':
#       #       direction = ""
#       #    else:                  => ordering_by = f'{direction.get(direction_to_sort_on,"-")}{field_to_sort_on}'
#       #       direction = "-"  
#    # def get_queryset(self):
#    #    return super().get_queryset()

#    def get_queryset(self):
#       q = self.request.GET.get('q')
#       qs = super().get_queryset()
#       if q:
#          my_filter = Q(book_description__contains=q)|Q(book_name__contains=q)
#          qs = qs.filter(my_filter).distinct()
#       return qs

#    def get_context_data (self, **kwargs):
#       context = super().get_context_data (**kwargs)
#       context ['page_title'] = "Books"
#       field_to_sort_on = self.request.GET.get('field')
#       direction_to_sort_on = self.request.GET.get ('direction')
#       q = self.request.GET.get('q')
#       context ['search_form'] = forms.SearchForm(
#          initial={
#             'q':q,
#             'field':field_to_sort_on,
#             'direction': direction_to_sort_on
#          })
#       context ['field_to_sort_on'] = field_to_sort_on
#       context ['direction_to_sort_on'] = direction_to_sort_on
#       return context

# #    def test_func (self):
#         # first_name = self.request.user.first_name 
#         # pk = self.request.user.pk
#         # return f"{pk}" == "1"

# class BookDetail (DetailView):
#    model = Book
# #    queryset = Book.objects.all() - work too

# class BookDelete (DeleteView):
#    success_url = reverse_lazy ('books-list')
#    model =  Book



# class BookCreate (CreateView):
#    model = Book
# #    fields = ('book_name', 'book_description')
#    success_url = reverse_lazy ('books-list')
#    form_class = forms.BookForm

# class BookUpdate (UpdateView):
#    model = Book
#    success_url ='/books-list/'
# #  form_class = forms.BookUpdate (needs to add form in forms.py)
#    fields = ('book_name', 'authors', 'book_description')







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




