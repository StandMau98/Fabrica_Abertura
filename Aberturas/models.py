from django.db import models

class Trabajo_PVC(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    imagen = models.ImageField(upload_to="Aberturas")
    date = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



    
class Trabajo_Aluminio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    imagen = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    

