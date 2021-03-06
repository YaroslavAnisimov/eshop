from django.views.generic import TemplateView, DetailView
# templateview - show template page
from references import models as ref_models
from . import models



class HomePage(TemplateView):
    template_name = 'cart\home-page.html'

    def get_context_data (self, **kwargs):
        context = super() .get_context_data(**kwargs)
        context ["authors"] = ref_models.Author.objects.all().order_by ("-pk")[:5]   
        return context

class UpdateCart(DetailView):
    model = models.Cart
    def get_object(self, *args, **kwargs):
        author_id = self.request.GET.get('author')
        if not author_id:
            #throw an error
            pass
        else:
            current_cart_pk = self.request.session.get(current_cart_pk)
            current_customer = self.request.user 
            if current_customer.is_anonymous:
                current_customer=None
            current_cart, cart_created = models.Cart.objects.get_or_create(
                pk = current_cart_pk,
                defaults= {'customer': current_customer}
            )
            print(cart_created, current_cart.pk)
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
                self.request.session['current_cart_pk']
            author = ref_models.Author.objects.get(pk=author_id)
            author_in_cart, author_created = models.AuthorInCart.objects.get_or_create(
                cart = current_cart,
                author = author,
                defaults = {'quantity': 1, 'price':book.price}
            )
            if not author_created:
                author_in_cart.quantity += 1
                author_in_cart.save()
        return current_cart

    #www.leningrad.ru/author/35/



