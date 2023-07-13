from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet)


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('api/signup/', views.Signup.as_view(), name='signup'),
    path('api/login/', views.Login.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/', views.User.as_view(), name='user'),
    # path('menu-items/', views.MenuItemList.as_view(), name='menu-item-list'),
    # path('menu-items/<int:pk>/', views.MenuItemDetail.as_view(), name='menu-item-detail'),
]

urlpatterns += router.urls