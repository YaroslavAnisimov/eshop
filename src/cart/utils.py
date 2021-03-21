from cart import models

def check_cart_owner(current_cart, current_customer):
    if current_cart.customer != current_customer:
        current_cart.customer = current_customer
        current_cart.save()


def update_books_count(request):
    current_cart_pk = request.session.get('current_cart_pk')
    if current_cart_pk:
        current_cart = models.CustomerCart.objects.get(pk=cart_pk)
        request.session['books_in_cart'] = current_cart.get_books_count


def update_items_in_cart(request):
    btn_action = None
    current_cart_pk = request.session.get('current_cart_pk')
    
    if current_cart_pk:
        cart = models.CustomerCart.objects.filter(pk=current_cart_pk).first()

        if not cart:
            return 
            
        cart_items = cart.books_in_cart.all()

        for item, value in request.GET.items():

            if item =='btn':
                action = value
                continue

            cart_item = cart_items.get(pk=item)

            if item and int(value) > 0:
                cart_item.qty = value
                cart_item.save()
            else:
                cart_item.delete()
    
        request.session['books_in_cart'] = cart.get_books_count
    return action












# from . import models

# def harvest_data(cbv_obj):
#     """Harvest all the data from the request
#     Args:
#         cbv_obj (cbv_obj):
#     Returns:
#         [tuple] : (current_cart_pk, cart_items)
#         """

#     current_cart_pk = cbv_obj.request.session.get('current_cart_pk')
#     cart_items = cbv_obj.self.request.GET
#     return current_cart_pk, cart_items

# def update_item_in_cart(cart_items_from_form, current_cart_pk):
#     action = None
#     cart = models.Cart.objects.filter(pk = current_cart_pk).first()
#     if not cart:
#         return
#     goods = cart.books.all()    
#     for name, quantity in cart_items_from_form.items():
#         if name == "btn":
#             action = quantity 
#             continue 
#         good = goods.filter(pk=name.split("_") [-1]).first()
#         if good and int(quantity)>0:
#             good.quantity = quantity
#             good.save()
#         else:
#             good.delete()
#     return action
    