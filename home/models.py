from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    What_do_you_want_to_automate = models.TextField(max_length=500)


    def __str__(self):
        return name