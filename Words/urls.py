from django.urls import path
from .views import HomePage, WordDetail, AddWords, as_viewss

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('<slug:slug>/', WordDetail.as_view(), name='detail_page'),
    path('add_words/', AddWords.as_view(), name='add_words'),
]