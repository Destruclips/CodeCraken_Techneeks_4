from django.db import models

# Create your models here.
class Contact_info(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    Query = models.TextField()
    def __str__(self):
        return self.name