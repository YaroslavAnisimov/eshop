
#show your login form if request is GET
#if request POST check user and login and redirect



from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect
from . import forms
from django.contrib.auth import authenticate, login, views
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = "accs/login.html"



# def login_view(request):
#     template_name = "accs/login.html"
#     if request.method =="GET":
#         login_form = forms.LoginForm()
#         return render(
#             request, 
#             template_name=template_name, context={"form":login_form})

#     elif request.method == "POST":
#         login_form = forms.LoginForm(request.POST)
#         if login_form. is_valid():
#             username = login_form.cleaned_data ['susername']
#             password = login_form.cleaned_data  ['password']
#             User = authenticate(request, username = username , password = password)
#             if user is not None:
#                 login (request, user)
#                 return HttpResponseRedirect(reverse('authors-list'))
#             else:
#                 return render(
#                 request,
#                 template_name=template_name,
#                 context ={"form": login_form})                
#         else:
#             return render(
#             request, 
#             template_name=template_name,
#             context={"form":login_form})