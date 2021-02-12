from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy 
from django.views.generic import DetailView, ListView, DeleteView, CreateView

from . import forms

# Create your views here.

from references.models import Author

#def authors_list (request):
#    authors = Author.objects.all()
#    context= {"authors": authors}
#    return render(request, template_name="home.html", context= context)

class AuthorsList (ListView) :
    model = Author



#def author_detail (request, pk):
#    author = Author.objects.get (pk = pk)
#    context= {"object": author}
#    return render(request, template_name="detail.html", context= context)

class AuthorDetail (DetailView):
    queryset = Author.objects.all()



#def author_delete (request, pk):
#    author = Author.objects.get (pk = pk)
#    Value = author.Value.all()
#    value_count = Value.count()
#    message = f'Author {author.name} with {value_count} values has just been deleted !'
#    Value.delete()
#    author.delete () 
#    context= {"message": message}
#    return render(request, template_name="delete.html", context= context)

class AuthorDelete(DeleteView):
    success_url = reverse_lazy ('authors-list-cbv/')
    model=Author 



def author_create (request):
    context = {}
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = form.save() 
            return HttpResponseRedirect (reverse ('author-detail', kwargs = {'pk': author.pk }))
        else:
            context['form'] = form

    else:
        context['form'] = forms.AuthorForm()

    return render(request, template_name="create.html", context= context)

class AuthorCreate (CreateView):
    model = Author
    success_url = reverse_lazy ('authors-list-cbv/')
    #form_class = forms.AuthorForm
    fields = ('name' , 'description')
 

def author_update (request):
    context= {}
    if request.metod == 'GET':
        author = Author.objects.get (pk =pk)
        
    elif request.method == 'POST':
        name = request.POST.get ('name')
        description = request.POST.get ('description')
        author = Author.objects.get (pk = pk) 
        author.name = name 
        author.description = description
        author.save()
        return HttpResponseRedirect (reverse ('author-detail', kwargs = {'pk': author.pk }))
    return render(request, template_name="update.html", context= context)


