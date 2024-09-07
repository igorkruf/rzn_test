from django.urls import path
from . import views


app_name="board"


urlpatterns = [
   path('',views.PageWithModalWindow.as_view(), name="test_modal"), 
   path('genres/', views.ListGenre.as_view(), name="list_genres"), 
   path('genres/<int:user_id>/', views.GetSecondPage.as_view(), name="second_page" ),
   path('calendar/', views.Calendar.as_view(), name="calendar"),
   path('xlsx/', views.MyView.as_view(), name="my_view")
   
]


