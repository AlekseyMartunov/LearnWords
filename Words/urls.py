from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('word/<slug:slug>/', views.WordDetail.as_view(), name='detail_view'),
    path('add_words/', views.AddWords.as_view(), name='add_words'),
    path('statistics/', views.Statistics.as_view(), name="statistics"),
]