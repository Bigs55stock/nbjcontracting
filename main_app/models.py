from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=250)
    number= models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    Inquiries= models.TextField(max_length=500)

   
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Projects(models.Model):

    brickwork = models.TextField(max_length=500)
    concrete= models.TextField(max_length=500)
    waterproofing = models.TextField(max_length=500)
    roofing = models.TextField(max_length=500)
    stucco = models.TextField(max_length=500)

   
    
    def __str__(self):
        return self.name

  