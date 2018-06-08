from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False) # field's value must be unique throughout the underlying databse table that is mapped. Every category must be unique, cannot be NULL.
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

