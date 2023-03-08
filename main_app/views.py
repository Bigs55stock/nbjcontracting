from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Customer
from .models import Projects
from .models import Manywork
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .forms import Customerform 
from django.http import HttpResponseRedirect



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

# class CustomerCreate(request):
#     return render(request, 'templates/customer_create.html', {})
    


class ManyworkDetail(DetailView):
    model = Manywork
    template_name = "manywork_detail.html"

def CustomerCreate(request):
    submitted = False
    if request.method == "POST":
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/customers/new/?submitted=True')
    else:
        form = Customerform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'customer_create.html', {'form':form, 'submitted':submitted})