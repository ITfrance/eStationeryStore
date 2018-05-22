from django.conf.urls import url
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='showcase'
urlpatterns = [
    path('search/', views.ResultView.as_view()), url('', views.IndexView.as_view()),
]