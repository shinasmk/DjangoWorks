"""vms URL Configuration

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
from vehicle import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicle/add',views.VehicleCreateView.as_view(),name="vehicle-add"),
    path('vehicles/all',views.VehicleListView.as_view(),name='vehicle-list'),
    path('vehicle/<int:pk>',views.VehicleDetailView.as_view(),name="vehicle-detail"),
    path('vehicle/change/<int:pk>',views.VehicleEditView.as_view(),name='vehicle-edit'),
    path('vehicle/remoove/<int:pk>',views.VehicleDeleteView.as_view(),name='vehicle-delete')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)