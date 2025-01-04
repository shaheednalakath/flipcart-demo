# from django import template
# register = template.Library()
#
#
# @register.filter(name='splitter')
# def splitter(lst_data, row_size):
#     rows = []
#     i = 0
#     for data in lst_data:
#         rows.append(data)
#         i += 1
#         if i == row_size:
#             yield rows
#             i = 0
#             rows = []
#     if rows:
#         yield rows
from django import template

register = template.Library()

@register.filter(name='splitter')
def splitter(lst_data, row_size):
    rows = []
    i = 0
    for data in lst_data:
        rows.append(data)
        i += 1
        if i == row_size:
            yield rows
            rows = []
            i = 0
    if rows:  # Yield any remaining items that don't fill a full row
        yield rows
