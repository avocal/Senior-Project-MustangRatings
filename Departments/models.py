from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_abrv = models.CharField(max_length=5)

    def __str__(self):
        return self.dept_abrv