from calendar import *
import locale
locale.setlocale(locale.LC_ALL, '')
# #########################################################
from django import template
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc

register = template.Library()

# def do_event_calendar(parser, token):
#     """
#     The template tag's syntax is {% event_calendar year month event_list %}
#     """

#     try:
#         tag_name, year, month, event_list = token.split_contents()
#     except ValueError:
#         raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]
#     return EventCalendarNode(year, month, event_list)

# class EventCalendarNode(template.Node):
#     """
#     Process a particular node in the template. Fail silently.
#     """

#     def __init__(self, year, month, event_list):
#         try:
#             self.year = template.Variable(year)
#             self.month = template.Variable(month)
#             self.event_list = template.Variable(event_list)
#         except ValueError:
#             raise template.TemplateSyntaxError

#     def render(self, context):
#         try:
#             # Get the variables from the context so the method is thread-safe.
#             my_event_list = self.event_list.resolve(context)
#             my_year = self.year.resolve(context)
#             my_month = self.month.resolve(context)
#             cal = EventCalendar(my_event_list)
#             return cal.formatmonth(int(my_year), int(my_month))
#         except ValueError:
#             return          
#         except template.VariableDoesNotExist:
#             return


class EventCalendar(LocaleHTMLCalendar):
    """
    Overload Python's calendar.HTMLCalendar to add the appropriate events to
    each day's table cell.
    """
   
   
    

    

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            # if day in self.events:
            #     cssclass += ' filled'
                body = '<ul>'
            # body = ['<ul>']
            #     for event in self.events[day]:
            #         body.append('<li>ddddddd')
            #         # body.append('<a href="%s">' % event.get_absolute_url())
            #         # body.append(esc(event.series.primary_name))
            #         # body.append('</a></li>')
            #         body.append('</li>')
            #     body.append('</ul>')
                return self.day_cell(cssclass, '<span class="dayNumber">%d</span> %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, '<span class="dayNumberNoEvents">%d</span>' % (day))
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month, my_previous_month, my_next_month,  my_previous_year, my_next_year):
        self.year, self.month = year, month
       
        # # Calculate values for the calendar controls. 1-indexed (Jan = 1)
        # my_previous_year = year
        # my_previous_month = month - 1
        # if my_previous_month == 0:
        #     my_previous_year = year - 1
        #     my_previous_month = 12
        # my_next_year = year
        # my_next_month =month + 1
        # if my_next_month == 13:
        #     my_next_year = year + 1
        #     my_next_month = 1
        # my_year_after_this =year + 1
        # my_year_before_this =year - 1



        v = []
        a = v.append
        a('<table  border="0" cellpadding="0" cellspacing="0" class="%s bordered " >' % (
            self.cssclass_month))
        a('\n')
        a(self.formatmonthname(self.year, self.month,  withyear=self.year, my_previous_month=my_previous_month,  my_next_month=my_next_month, my_previous_year=my_previous_year, my_next_year=my_next_year))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(self.year, self.month):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def group_by_day(self, events):
        field = lambda event: event.date_and_time.day
        return dict(
            [(day, list(items)) for day, items in groupby(events, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
    
    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (
            self.cssclasses_weekday_head[day], day_name[day])

# Register the template tag so it is available to templates




1






# locale.setlocale(locale.LC_ALL, "ru_RU")
# class FullScreenCalendar(LocaleHTMLCalendar):
#     '''
#     Календарь на всю страницу
#     '''

#     def formatmonth(self, theyear: int, themonth: int, withyear: bool = True) -> str:
#         self.cssclass_month=f'{self.cssclass_month} w100'
#         return super().formatmonth(theyear, themonth, withyear)
    
#     def formatday(self, day: int, weekday: int) -> str:
        
#         return super().formatday(day, weekday)