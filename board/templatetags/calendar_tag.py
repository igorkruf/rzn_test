from django import template
from calendar import HTMLCalendar
from datetime import date
# from board.utils import FullScreenCalendar 

register = template.Library()

# @register.simple_tag()
# def get_tree(node):
#     list_parents=node.get_tree(node)
#     return list_parents

# @register.inclusion_tag('board/inclusion_calendar.html')
# def show_calendar_of_curent_month(curent_date:date):
#     cal= FullScreenCalendar(locale="ru")
#     print('hhhhhhhhhhhhhhhhhh')
#     print(cal.cssclasses)
#     print('gggggggggggggg')
#     curent_month=curent_date.month
#     curent_year=curent_date.year
#     month=cal.formatmonth(curent_year, curent_month)
#     return {"calendar": month}
