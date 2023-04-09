from django import urls
from django.urls import path,include
from books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.BookListView.as_view(),name='home'),
    path('',views.IndexView.as_view(),name='index'),
    path('register',views.SignUpView.as_view(),name='signup'),
    path('signin',views.SignInView.as_view(),name='signin'),
    path('signout',views.SignOutView.as_view(),name='signout'),
    path('bookdetail/<int:pk>',views.BookDetailView.as_view(),name='book-details')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  