from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


# Create your models here.
class Review(models.Model):

    # Foreign key linking this review to a user
    creator = models.ForeignKey(User)
    # Unique char name for the review
    name = models.CharField(max_length=128,primary_key=True,unique=True)
    # user description of query
    description = models.TextField(default="")
    #date review started
    date_started = models.DateField(default=date.today())
    #Total papers in pool
    pool_size=models.IntegerField(default=0)
    #number of abstracts judged
    abstracts_judged=models.IntegerField(default=0)
    #number of documents judged
    document_judged=models.IntegerField(default=0)
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
    query_string = models.TextField()
    # Number of results returned from query
    pool_size = models.IntegerField(default=0)
    # previous results to correlate with (IDs stored as a comma separated string)
    results = models.TextField()

    def __unicode__(self):
        return self.query_string

class Researcher(models.Model):
    # The user the profile is linked to
    user = models.ForeignKey(User)

    # The user's first name
    name = models.CharField(max_length=50,unique=False)

    # The user's surname
    surname = models.CharField(max_length=50,unique=False,blank=True)

    # The user's bio
    bio = models.CharField(max_length=500,unique=False,blank=True)

    # The user's institution
    institution = models.CharField(max_length=100,unique=False,blank=True)

    # The reviews started by the user
    reviews = models.ManyToManyField(Review,blank=True)


    # The currently selected review
    selected_review = models.CharField(max_length=128,blank=True)

    def __unicode__(self):
        return self.name

class Paper(models.Model):
    # The review that contains the Document
    review = models.ForeignKey(Review)

    # Title of the Document returned by the API
    title = models.TextField()

    # Authors of the Document returned by the API
    authors = models.TextField()

    # Abstract of the Document returned by the API
    abstract = models.TextField()

    # Publish date of the Document returned by the API
    publish_date = models.DateField(default=date.today())

    # Link to the Document returned by the API
    paper_url = models.URLField()

    # ID of the Document returned by the API
    #pubmedID = models.CharField(max_length=128)
    # Citations for the Document returned for the API
    #citation = models.CharField(max_length=128)

    # which pool is this paper in?
    abstract_relevance = models.BooleanField(default=False)
    document_relevance = models.BooleanField(default=False)

    # notes option
    notes = models.TextField(default="")

    def __unicode__(self):
        return self.title