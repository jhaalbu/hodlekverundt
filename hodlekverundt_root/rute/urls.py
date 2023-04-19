from django.urls import path, include
from rute import views

app_name = 'rute'

urlpatterns = [
    path('', views.alle_ruter, name='alle_ruter'),
    path('<int:pk>', views.rute_detail, name='rute_detail'),
    path('kart/', views.kart, name='kart'),
    path('kart2/', views.kart2, name='kart2'),
    path('kart3/', views.kart3, name='kart3')

]
