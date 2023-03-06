from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=100)
    number= models.CharField(max_length=250)
    email = models.TextField(max_length=500)
    typeofwork= models.CharField(max_length=250)

   
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
