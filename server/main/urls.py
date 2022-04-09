from django.urls import path
from . import views


urlpatterns = [
    path('main', views.index, name='home'),
    path('<int:main_id>/', views.test, name='show')
]
