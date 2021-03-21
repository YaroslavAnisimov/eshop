from django.views.generic import TemplateView, DetailView, RedirectView
from django.urls import reverse
# templateview - show template page
from references import models as ref_models
from . import models
from . import utils 



class HomePage(TemplateView):
    template_name = 'cart\home-page.html'

    def get_context_data (self, **kwargs):
        context = super() .get_context_data(**kwargs)
        context ["books"] = ref_models.Book.objects.all().order_by ("-pk")[:5]   
        return context

class UpdateCart(DetailView):
    model = models.Cart
    def get_object(self, *args, **kwargs):
        book_id = self.request.GET.get('book')
        if not book_id:
            current_cart_pk = self.request.session.get('current_cart_pk')
            if current_cart_pk:
                current_cart = models.Cart.objects.filter(pk = current_cart_pk).first()
                return current_cart or []
            return []
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
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
            book = ref_models.Book.objects.get(pk=book_id)
            book_in_cart, book_created = models.BookInCart.objects.get_or_create(
                cart = current_cart,
                book = book,
                defaults = {'quantity': 1, 'price': book.price}
            )
            if not book_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return current_cart

    #www.leningrad.ru/book/35/

class RecalculateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return_urls = {
            'checkout': reverse("cart:checkout")
        }
        current_cart_pk, cart_items = utils.harvest_data(self)
        if not current_cart_pk:
            return reverse ("cart:add_to_cart")
        action = utils.update_items_in_cart(current_cart_pk, cart_items_from_form)
        # action = checkout or recalculate
        if action == "checkout":
            url = reverse ("cart:checkout")
        else:
            reverse("cart:add_to_cart")
        return url


