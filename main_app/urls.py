from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name="about"),
    path('projects/', views.ProjectsList.as_view(), name="projects_list"),
    path('projects/<int:pk>/', views.ManyworkDetail.as_view(), name="manywork_detail"),
    path('customers/new/', views.CustomerCreate, name="customer_create"),
    path('customer/success', views.Success.as_view(), name="success"), 
]