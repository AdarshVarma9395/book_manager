from django.db import models

class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)   
    author = models.CharField(max_length=255)  
    published_date = models.DateField(null=True, blank=True)  
    is_available = models.BooleanField(default=True)  

    def __str__(self):
        return self.title
