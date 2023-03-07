from django.contrib import admin
from .models import Customer 
from .models import Projects 
from .models import Manywork 

# Register your models here.
admin.site.register(Customer)
admin.site.register(Projects)
admin.site.register(Manywork)