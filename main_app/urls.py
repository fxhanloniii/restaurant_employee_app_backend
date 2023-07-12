from django.urls import path
from . import views
from .views import MenuItemList, MenuItemDetail

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('api/signup/', views.Signup.as_view(), name='signup'),
    path('api/login/', views.Login.as_view(), name='login'),
    path('api/user/', views.User.as_view(), name='user'),
    path('menu-items/', MenuItemList.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', MenuItemDetail.as_view(), name='menu-item-detail'),
]