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

    typeofwork = models.TextField(max_length=500)
    img= models.TextField(max_length=500)
   
    
    def __str__(self):
        return self.typeofwork


class Manywork(models.Model):

    name = models.TextField(max_length=500)
    img = models.TextField(max_length=500)
    desc= models.TextField(max_length=500)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
  