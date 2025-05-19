from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tab1/', views.tab1, name='tab1'),
    path('tab2/', views.tab2, name='tab2'),
    path('tab3/', views.tab3, name='tab3'),
    path('upload/', views.upload_paper, name='upload'),
]
