from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):

    # Foreign key linking this review to a user
    researcher = models.ForeignKey(User)
    # Unique char name for the review
    name = models.CharField(max_length=128,primary_key=True,unique=True)
    # Slug for url paths
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Query(models.Model):
    # Queries are identified by their relation to a review
    review = models.ForeignKey(Review,unique = True)
    # Name of the query given by the user
    query_string = models.TextField()
    # Number of results returned from query
    pool_size = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    # The user the profile is linked to
    user = models.ForeignKey(User)

    # The user's first name
    name = models.CharField(max_length=50,unique=False)

    # The user's surname
    surname = models.CharField(max_length=50,unique=False)

    # The user's bio
    bio = models.CharField(max_length=500,unique=False)

    # The user's institution
    institution = models.CharField(max_length=100,unique=False)

    # The reviews started by the user
    reviews = models.ManyToManyField(Review)

    # The currently selected review
    current_review = models.CharField(max_length=128,unique=False)

    def __unicode__(self):
        return self.name


class Document(models.Model):
    # The review that contains the Document
    review = models.ForeignKey(Review)

    # Title of the Document returned by the API
    title = models.TextField()

    # Authors of the Document returned by the API
    authors = models.TextField()

    # Abstract of the Document returned by the API
    abstract = models.TextField()

    # Publish date of the Document returned by the API
    #publish_date=models.DateField()

    # Link to the Document returned by the API
    documentURL = models.URLField()

    #DocumentFree = models.BooleanField()

    # ID of the Document returned by the API
    #pubmedID = models.CharField(max_length=128)
    # Citations for the Document returned for the API
    #citation = models.CharField(max_length=128)

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

    # notes option
    notes = models.TextField(default="")

    def __unicode__(self):
        return self.title