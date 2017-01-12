from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return(self.name)
    
    def __repr__(self):
        return(self.name)
    
    