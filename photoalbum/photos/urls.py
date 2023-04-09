from django.contrib import admin
from django.urls import path
from photos import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery',views.GalleryHomeView.as_view(),name='home'),
    path('gallery/photo/<int:pk>',views.PhotoView.as_view(),name='photo-detail'),
    path('gallery/photo/add',views.addPhotoView,name='photo-add'),
]