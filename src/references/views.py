from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.db.models import Q
from . import forms

from references.models import Author

# (UserPassesTestMixin, ListView) 

class AuthorsList (LoginRequiredMixin, ListView) :
   model = Author
   login_url = '/admin/login/'
   paginate_by = 10 

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
      context ['page_title'] = "Authors"
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

class AuthorDetail (DetailView):
    model = Author
#    queryset = Author.objects.all()

class AuthorDelete (DeleteView):
   success_url = reverse_lazy ('authors-list')
   model = Author 


class AuthorCreate (CreateView):
   model = Author
#    fields = ('name', 'description')
   success_url = reverse_lazy ('authors-list')
   form_class = forms.AuthorForm

class AuthorUpdate (UpdateView):
    model = Author
    success_url ='/authors-list/'
    fields = ('name', 'description')



# def author_update (request):
#     context= {}
#     if request.metod == 'GET':
#         author = Author.objects.get (pk =pk)
#         context = {'name': author.name, 'description': author.description}
#     elif request.method == 'POST':
#         name = request.POST.get ('name')
#         description = request.POST.get ('description')
#         author = Author.objects.get (pk = pk)
#         author.name = name 
#         author.description = description
#         author.save()
#         return HttpResponseRedirect (reverse ('author-detail', kwargs = {'pk': author.pk }))
#     return render(request, template_name="update.html", context= context)




# def authors_list (request):
#     authors = Author.objects.all()
#     context= {"authors": authors}
#     return render(request, template_name="home.html", context= context)

# def author_detail (request, pk):
#     author = Author.objects.get (pk = pk)
#     context= {"object": author}
#     return render(request, template_name="detail.html", context= context)

# def author_delete (request, pk):
#     author = Author.objects.get (pk = pk)
#     Opinions = author.Opinions.all()
#     Opinions_count = Opinions.count() 
#     message = f'Author {author.name} with {Opinions_count} reviews has just been deleted !'
#     Opinions.delete()
#     author.delete () 
#     context= {"message": message}
#     return render(request, template_name="delete.html", context = context)

# def author_create(request):
#     if request.method == 'POST':
#         name = request.POST.get ('name')
#         description= request.POST.get ('description')
#         author = Author.objects.create (name = name , description = description)
#         return HttpResponseRedirect (reverse('author-detail', kwargs = {'pk':author.pk}))
#     context = {'form': forms.AuthorForm()}
#     return render (request, template_name = "create.html", context = context)


# def author_create (request):
#     context = {}
#     if request.method == 'POST':
#        form = forms.AuthorForm(request.POST)
#        if form.is_valid():
#            author = form.save() 
#            return HttpResponseRedirect (reverse ('author-detail', kwargs = {'pk': author.pk }))
#        else:
#            context['form'] = form
#     else:
#        context['form'] = forms.AuthorForm()
#     return render(request, template_name="create.html", context= context)




