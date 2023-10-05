from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view(), name='index'),
    path('menu', views.MenuItemView.as_view(), name='menu-item'),
    path('menu/<int:id>', views.SingleMenuItemView.as_view(), name='single-item'),
]