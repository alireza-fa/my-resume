from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.HomeFaView.as_view(), name='home_fa'),
    path('en/', views.HomeEnView.as_view(), name='home_en'),
]
