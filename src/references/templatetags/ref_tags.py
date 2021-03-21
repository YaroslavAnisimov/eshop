# from django.conf import settings
# from django.utils.safestring import mark_safe
# from django import template

# register = template.Library()

# @register.simple_tag
# def company_name(prefix):
#     return prefix + " " + settings.COMPANY_NAME



# @register.simple_tag
# def arrow(td_book_name, field_to_sort_on, direction_to_sort_on):
#     if field_to_sort_on == td_book_name and direction_to_sort_on == 'up':
#         return mark_safe('<i class="fas fa-angle-up"></i>')
#     elif field_to_sort_on == td_book_name and direction_to_sort_on == 'down':
#         return mark_safe('<i class="fas fa-angle-up"></i>')
#     return ""



# @register.simple_tag
# def strange_summ(book_obj):
#     pk = book_obj.pk
#     books = book_obj.books.all().count()
#     summ = pk + books
#     return summ 



