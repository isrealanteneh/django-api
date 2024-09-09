from django.db import models

# Create your models here.
class Orga_Structure(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    parentId = models.IntegerField(null=True)

    def __str__(self):
        return self.name