from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) # blank=True allows us to have blank usrls

    def __str__(self):            # This resturns what the default name is returned when someone looks at one of these objects
        return self.title
