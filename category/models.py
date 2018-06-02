from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=15)

    floor = models.PositiveIntegerField(db_index=True)

    class Meta:
        ordering = ('floor',)

    def __str__(self):
        return self.title


class Kinds(models.Model):
    description = models.CharField(max_length=200)
    to_category = models.ForeignKey(Category, related_name='c_kinds', on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.description




