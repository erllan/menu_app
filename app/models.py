from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    parent = models.ForeignKey('Menu', related_name='children_menu', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
