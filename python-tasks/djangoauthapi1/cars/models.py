from django.db import models


# Create your models here.

class Car(models.Model):
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=50, unique=True)
    cat_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cars'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'
