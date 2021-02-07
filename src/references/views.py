from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from references.models import Author

def home_page (request):
    authors = Author.objects.last()
    context= {"books": books}
    return render(request, template_name="home.html", context= context)


