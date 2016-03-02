from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    # Primary key for the review is a 128 char name
    name = models.CharField(max_length=128, unique=True, primary_key=True)
    # Slug for url paths
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Query(models.Model):
    # Queries are identified by their relation to a review
    review = models.ForeignKey(Review)
    # Name of the query given by the user
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50,unique=False)
    surname = models.CharField(max_length=50,unique=False)
    bio = models.CharField(max_length=500,unique=False)
    institution = models.CharField(max_length=100,unique=False)
    reviews = models.ManyToManyField(Review)

    def __unicode__(self):
        return self.name


class Document(models.Model):
    review = models.ForeignKey(Review)
    # Title of the document returned by the API
    title = models.TextField()
    # Authors of the document returned by the API
    authors = models.TextField()
    # Abstract of the document returned by the API
    abstract = models.TextField()
    # Link to the document returned by the API
    documentURL = models.URLField()

    #documentFree = models.BooleanField()

    # ID of the document returned by the API
    pubmedID = models.CharField(max_length=128)
    # Citations for the document returned for the API
    citation = models.CharField(max_length=128)

    # abstractPool = models.BooleanField(default=True)
    # documentPool = models.BooleanField(default=False)
    # finalPool = models.BooleanField(default=False)

    # Is this document in the abstract, document or final pool?
    POOL_CHOICES = (
        (1,"Abstract"),
        (2,"Document"),
        (3,"Final"),
    )
    currentPool = models.IntegerField(choices=POOL_CHOICES,default=1)

    def __unicode__(self):
        return self.title