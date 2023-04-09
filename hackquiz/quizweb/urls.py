from django import urls
from django.urls import path

from quizweb import views as web_view


urlpatterns=[
    path("home",web_view.IndexView.as_view(),name='home'),
    path('register',web_view.SignUpView.as_view(),name="signup"),
    path('login',web_view.SignInView.as_view(),name="signin"),
    path('quiz/home',web_view.QuizHomeView.as_view(),name='quiz-home'),
    path('question/all/<str:cat>/<str:mode>/',web_view.QuestionListView.as_view(),name="question-list"),
    path('quiz/all',web_view.QuizLIstView.as_view(),name="history"),
    path('logout',web_view.SignOutView.as_view(),name='logout')


]