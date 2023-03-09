from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Customer
from .models import Projects
from .models import Manywork
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
# from .forms import Customerform 
from django.http import HttpResponseRedirect
from .forms import ContactForm



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

# class ProjectsList(TemplateView):
#     template_name = "projects_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["projects"] = Projects.objects.all() 
#         return context

class ProjectsList(TemplateView):
    template_name = "projects_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["projects"] = Projects.objects.filter(name__icontains=typeofwork)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["projects"] = Projects.objects.all()
            # default header for not searching 
            context["header"] = f"Search"
        return context        


class ManyworkDetail(DetailView):
    model = Projects
    template_name = "manywork_detail.html"
    

# def CustomerCreate(request):
#     submitted = False
#     if request.method == "POST":
#         form = Customerform(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/customers/new/?submitted=True')
#     else:
#         form = Customerform
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'customer_create.html', {'form':form, 'submitted':submitted})




def CustomerCreate(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'customer_create.html', context)


