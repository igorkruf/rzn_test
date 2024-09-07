from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic.base import ContextMixin
from django.views import View
from .models import Genre
from datetime import datetime, date
import calendar
from .utils import EventCalendar
import io
from django.http import HttpResponse
from django.views.generic import View
import xlsxwriter
# Create your views here.

class ListGenre(ContextMixin, View):
    '''
    Тестовое представление Жанры(древовидная структура)
    '''


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        list_genres=Genre.objects.all()
        context['genres']=list_genres
        return context
    

    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        context['url']="board:second_page"
        context['user_id']= 3
        return render(req, 'board/base.html', context)

class GetSecondPage(ContextMixin, View):
    '''
    Тестовое представление Жанры(древовидная структура)
    '''


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        list_genres=Genre.objects.all()
        context['genres']=list_genres
        return context
    

    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        
        return render(req, 'board/second_page.html', context)


class Calendar(ContextMixin, View):
    '''
    Тестовая страница с календарём
    '''
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        datetime_today=datetime.now()
        month= int(req.GET.get('month')) if req.GET.get('month') else datetime_today.month
        year= int(req.GET.get('year'))   if req.GET.get('year') else datetime_today.year
        my_year = int(year)
        my_month = int(month)
        # Calculate values for the calendar controls. 1-indexed (Jan = 1)
        my_previous_year = my_year-1
        my_previous_month = my_month - 1
        if my_previous_month == 0:
            my_previous_year = my_year - 1
            my_previous_month = 12
            my_next_year = my_year
            my_next_month = my_month + 1
        if my_next_month == 13:
            my_next_year = my_year + 1
            my_next_month = 1
        # my_year_after_this = my_year + 1
        # my_year_before_this = my_year - 1
        
        
        calendar=EventCalendar()
        
        cal=calendar.formatmonth(year, month, my_previous_month, my_next_month,  my_previous_year, my_next_year)
        context['calendar']=cal
        


        return render(req, 'board/calendar_page.html', context)
    
class PageWithModalWindow(ContextMixin, View):
    '''
    Тестовая страница с модальным окном
    '''

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        return render(req, 'board/base.html')
    

def get_simple_table_data():
    # Simulate a more complex table read.
    return [['1jksgfdkjfs kjsfkjf gaggafgakjfgkajgfjagag', 2, 3], [4, 5, 6], [7, 8, 9]]


class MyView(View):
    def get(self, request):
        # Create an in-memory output file for the new workbook.
        output = io.BytesIO()

        # Even though the final file will be in memory the module uses temp
        # files during assembly for efficiency. To avoid this on servers that
        # don't allow temp files, for example the Google APP Engine, set the
        # 'in_memory' Workbook() constructor option as shown in the docs.
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        # Get some data to write to the spreadsheet.
        data = get_simple_table_data()

        # Write some test data.
        for row_num, columns in enumerate(data):
            for col_num, cell_data in enumerate(columns):
                worksheet.write(row_num, col_num, cell_data)

        # Close the workbook before sending the data.
        workbook.close()

        # Rewind the buffer.
        output.seek(0)

        # Set up the Http response.
        filename = "django_simple.xlsx"
        response = HttpResponse(
            output,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = "attachment; filename=%s" % filename

        return response