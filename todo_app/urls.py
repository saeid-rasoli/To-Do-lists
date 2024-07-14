from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='list'),
    path('list/add/', views.ListCreate.as_view(), name='list_add'),
    path('list/<int:list_id>/item/add/', views.ItemCreate.as_view(), name='item_add'),
    path('list/<int:list_id>/item/<int:pk>/', views.ItemUpdate.as_view(), name='item_update')
]
