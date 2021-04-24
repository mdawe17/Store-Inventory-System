from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [   
    path('search/', views.search, name = "Search"),
    path('create/', views.createItem, name = "Create"),
    path('retire/<int:pk>/', views.deleteOrder, name = "retire"),
    path('searchresults/', views.search_results, name = 'searchResults'),
    path('update/<int:pk>/', views.updateItems, name = 'update_items'),
    path('', views.loginPage, name = 'login'),
    path('home/', views.homePage, name = 'home')
]