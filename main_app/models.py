from django.db import models


class Projects(models.Model):

    typeofwork = models.TextField(max_length=500)
    img= models.TextField(max_length=500)
   
    
    def __str__(self):
        return self.typeofwork

    class Meta:
        ordering = ['typeofwork']


class Manywork(models.Model):

    name = models.TextField(max_length=500)
    img = models.TextField(max_length=500)
    desc= models.TextField(max_length=500)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE , related_name = "work")
    
    
    def __str__(self):
        return self.name
  


class Customer(models.Model):

    name = models.CharField(max_length=250)
    number= models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message= models.TextField(max_length=500)

    
    def __str__(self):
        return self.name


