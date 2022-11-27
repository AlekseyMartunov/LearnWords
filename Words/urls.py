from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('word/<slug:slug>/', views.WordDetail.as_view(), name='detail_view'),
    path('add_words/', views.AddWords.as_view(), name='add_words'),
    path('study/', views.Study.as_view(), name='study')
]