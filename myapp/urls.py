from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns =[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('appointment/', views.appointment, name='appointment'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    
    

]