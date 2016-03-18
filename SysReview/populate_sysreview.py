import os
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SysReview.settings')

import django
django.setup()

from mainapp.models import Review, Paper, Query, Researcher
from django.contrib.auth.models import User

#population script for sysreview database
def populate():

    #list of users created, used for printing to cmd line as user object not iterable
    createdUsers=[]

    #create 1st user
    user1= add_user('jill')
    #add new user to list
    createdUsers.append(user1)
    #create reviews
    user1review1 = add_review(creator=user1,name="Effects of diabetes")
    #create queries

    #create 2nd user
    user2= add_user('bob')
    #add new user to list
    createdUsers.append(user2)
    #create reviews
    user1review1 = add_review(creator=user2,name="Effects of asthma")
    #create queries

    #create 3rd user
    user3= add_user('jen')
    #add new user to list
    createdUsers.append(user3)
    #create reviews
    user1review1 = add_review(creator=user3,name="Effects of high blood pressure")
    #create queries


    # Print out what we have added to the user.
    for createdUser in createdUsers:
        for review in Review.objects.filter(creator=createdUser):
            print "User - {0}, Review - {1}, Review queries -".format(str(createdUser), str(review))

def add_user(username):
    user, created= User.objects.get_or_create(username=username)
    user.set_password(username)
    user.email = username + "@" + username +".com"
    user.save()
    researcher, created = Researcher.objects.get_or_create(user=user,name=username)
    researcher.surname = username
    researcher.bio = "This is "+ username +" bio."
    researcher.institution = "University of Glasgow"
    researcher.save()
    return user

def add_review(creator,name):
    review = Review.objects.get_or_create(creator=creator, name=name)[0]
    review.save()
    return review

if __name__=='__main__':
    print "Starting SysReview population script..."
    populate()
