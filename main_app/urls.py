from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name="about"),
    path('projects/', views.ProjectsList.as_view(), name="projects_list"),
    path('customers/new/', views.CustomerCreate.as_view(), name="customer_create")
]
