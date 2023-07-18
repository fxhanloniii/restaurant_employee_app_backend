from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet)
router.register(r'cocktails', views.CocktailViewSet)
router.register(r'wines', views.WineViewSet)

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('api/signup/', views.Signup.as_view(), name='signup'),
    path('api/login/', views.Login.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/', views.User.as_view(), name='user'),
]

urlpatterns += router.urls
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)