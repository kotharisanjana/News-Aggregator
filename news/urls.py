from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_headlines, name='topheadlines'),
    path('allnews/', views.categorywise_news, name='categorywisenews'),
    path('allnews/search', views.search, name='search')
]