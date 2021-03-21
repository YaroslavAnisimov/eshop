from django.shortcuts import render
from django.contrib.auth import forms as auth_forms, views as auth_views, models as auth_models, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from users import urls, forms, models
# Create your views here.


class UserCreationView(generic.CreateView):
    model = auth_models.User
    form_class = auth_forms.UserCreationForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('users:update-user')

    def get_success_url(self, *args, **kwargs):
        username=self.request.POST.get('username')
        password=self.request.POST.get('password1')
        user = authenticate(self.request, username=username, password=password)
        user.groups.add(auth_models.Group.objects.get(name='Customers'))
        user.save()
        # user_ext, created = models.ExtUserData.objects.get_or_create(pk=user.pk)
        
        if user is not None:
            login(self.request, user)        
        
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")

        return str(self.success_url)


class UserLoginView(auth_views.LoginView):
    template_name='users/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()

        if url in ['/users/login/', '', None]:
            url = reverse_lazy('homepage')  
        return url


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('homepage')    


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = auth_models.User
    form_class = forms.UserProfileForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('users:update-user')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        ext_user_data, created = models.ExtUserData.objects.get_or_create(pk=self.request.user.pk)
        ext_user_data.save()
        context['form_ext'] = forms.UserProfileExtForm(instance=ext_user_data)
        return context

    def form_valid(self, form):
        self.object = form.save()
        object_ext = models.ExtUserData.objects.get(pk=self.request.user.pk)
        form_ext = forms.UserProfileExtForm(self.request.POST, instance=object_ext)

        if form_ext.is_valid():
            object_ext = form_ext.save()

        return super().form_valid(form)

    def get_object(self, **kwargs):
        return self.request.user



#show your login form if request is GET
#if request POST check user and login and redirect



# from django.shortcuts import render
# from django.urls import reverse 
# from django.http import HttpResponseRedirect
# from . import forms
# from django.contrib.auth import authenticate, login, views
# from django.contrib.auth.views import LoginView


# class MyLoginView(LoginView):
#     template_name = "accs/login.html"



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