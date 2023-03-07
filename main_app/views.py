from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Customer
from .models import Projects
from .models import Manywork
from django.views.generic.edit import CreateView



class Home(View):

    def get(self, request):
        return HttpResponse("NBJ Home")


class About(View):

    def get(self, request):
        return HttpResponse("NBJ About")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class ProjectsList(TemplateView):
    template_name = "projects_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Projects.objects.all() 
        return context

class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'number', 'email', 'Inquiries']
    template_name = "customer_create.html"
    success_url = "/projects/"