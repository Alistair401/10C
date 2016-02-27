from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Query(models.Model):
    review = models.ForeignKey(Review)
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Document(models.Model):
    review = models.ForeignKey(Review)

    title = models.TextField(unique=True)
    authors = models.TextField()
    abstract = models.TextField()
    documentURL = models.URLField()
    documentFree = models.BooleanField()
    pubmedID = models.CharField(max_length=128)
    citation = models.CharField(max_length=128)

    abstractPool = models.BooleanField(default=True)
    documentPool = models.BooleanField(default=False)
    finalPool = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title