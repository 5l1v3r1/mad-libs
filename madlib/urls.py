from django.conf.urls import url
from madlib import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^romantic_poetry/$', views.RomanticPoetryView.as_view()),
]
