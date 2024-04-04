from django.db import models

class Recipe(models.Model):
    ID = models.IntegerField(primary_key=True,default=None)
    name = models.CharField(max_length=100)
    description = models.TextField()
    cuisine = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    prep_time = models.CharField(max_length=50, null=True, blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    full_text = models.TextField()


    def __str__(self):
        return self.name



