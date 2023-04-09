"""olxClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api import views
from myapp import views as myapp_api_views
from mywebapp import views as my_webapp_views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("categories",views.CategoryView,basename='categories')
router.register("users",views.UserView,basename="users")

router.register('api/v2/users',myapp_api_views.RegistationView,basename="accounts")
router.register('api/v2/category',myapp_api_views.CategoriesView,basename='category')
router.register('api/v2/vehicle',myapp_api_views.VehicleView,basename='vehicles')
router.register('api/v2/wishlists',myapp_api_views.WishlistView,basename='wishlist')
router.register('api/v2/questions',myapp_api_views.QuestionsView,basename='questions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vehicles',views.VehicleView.as_view()),
    path('api/vehicles/<int:pk>',views.VehicleDetailView.as_view()),
    path('api/v2/token/',ObtainAuthToken.as_view()),
    path('home',my_webapp_views.HomeView.as_view(),name='home'),
    path('register',my_webapp_views.SignUpView.as_view(),name='signup'),
    path('signin',my_webapp_views.SignInView.as_view(),name='signin'),
    path('signout',my_webapp_views.SignOutView.as_view(),name='logout'),
    path('vehicle/add',my_webapp_views.VehicleAddView.as_view(),name='vehicle-add'),
    path('home2',my_webapp_views.VehicleAddHomeView.as_view(),name="home22")
]+router.urls
