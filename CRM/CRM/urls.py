"""CRM URL Configuration

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
from erp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/add',views.EmployeeCreateView.as_view(),name='emp-add'), 
    path('',views.IndexView.as_view(),name='home'),
    path('base',views.BaseView.as_view(),name='base'),
    path('employees/all',views.EmployeeListView.as_view(),name='emp-list'),
    path('employees/<int:pk>',views.EmployeeDetailView.as_view(),name='emp-detail'),
    path('employees/remove/<int:pk>',views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path('employee/change/<int:pk>',views.EmployeeEditView.as_view(),name="emp-edit"),
    path('register',views.RegistratiomView.as_view(),name="register"),
    path('signin',views.SignInView.as_view(),name='signin'),
    path('signout',views.SignOutView.as_view(),name='signout'),
    path('emphome',views.EmpHomeView.as_view(),name="emp-home"),
    path('course/add',views.CourseCreateView.as_view(),name="course-add"),
    path('course/all',views.CourseListView.as_view(),name="course-list"),
    path('course/<int:pk>',views.CourseDetailView.as_view(),name="course-detail"),
    path('course/remove/<int:pk>',views.course_delete_view,name="course-delete"),  #as_view is not used because it is function view
    path('course/change/<int:pk>',views.CourseEditView.as_view(),name="course-edit"),
    path('coursehome',views.CourseHomeView.as_view(),name="course-home"),
    path('batch/add',views.BatchCreateView.as_view(),name="batch-add"),
    path('batch/<int:pk>',views.BatchDetailView.as_view(),name="batch-detail"),
    path("batch/change/<int:pk>",views.BatchEditView.as_view(),name="batch-edit"),
    path('batch/remove/<int:pk>',views.batch_delete_view,name="batch-delete"),
    path('batchhome',views.BatchHomeView.as_view(),name="batch-home"),
    path("student/add",views.StudentCreateView.as_view(),name="student-add"),
    path("student/all",views.StudentListView.as_view(),name="student-list"),
    path("student/<int:pk>",views.StudentDetailView.as_view(),name="student-detail"),
    path("student/remove/<int:pk>",views.StudentDeleteView.as_view(),name="student-delete"),
    path("student/change/<int:pk>",views.StudentEditView.as_view(),name="student-edit"),
    path("studenthome",views.StudentHomeView.as_view(),name="student-home"),
    path("facultyhome",views.FacultyHomeView.as_view(),name="faculty-home"),
    path('faculty/add',views.FacultyCreateView.as_view(),name="faculty-add"),
    path('faculty/all',views.FacultyListView.as_view(),name="faculty-list"),
    path('faculty/<int:pk>',views.FacultyDetailView.as_view(),name='faculty-detail'),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
