import os
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SysReview.settings')

import django
django.setup()

from mainapp.models import Review, Paper, Query, Researcher
from django.contrib.auth.models import User


# Systematic eaxmaple review titles taken from http://www.cochranelibrary.com/cochrane-database-of-systematic-reviews/
# only titles used no other aspect or content of reviews used

#population script for sysreview database, create 3 users with 3 reviews
def populate():

    #list of users created, used for printing to cmd line as user object not iterable
    createdUsers=[]

    #create 1st user
    user1= add_user('jill')
    #add new user to list
    createdUsers.append(user1)
    #create reviews
    user1review1 = add_review(creator=user1,name="Interventions for preventing falls in older people living in the community")
    user1review2 = add_review(creator=user1,name="Exercise for depression")
    user1review3 = add_review(creator=user1,name="Early skin-to-skin contact for mothers and their healthy newborn infants")
    #create queries
    create_query(user1review1,"(((((((((((((Interventions ) AND preventing ) AND accidental falls) OR accidental) AND older) AND persons) OR people) AND life) OR living) AND residence characteristics) OR residence) AND characteristics) OR residence characteristics) OR community ")
    create_query(user1review2,"(((((exercise) AND depressive disorder) OR depressive) NOT disorder) OR depressive disorder) OR depression ")
    create_query(user1review3,"")

    #create 2nd user
    user2= add_user('bob')
    #add new user to list
    createdUsers.append(user2)
    #create reviews
    user2review1 = add_review(creator=user2,name="Neuraminidase inhibitors for preventing and treating influenza in healthy adults and children")
    user2review2 = add_review(creator=user2,name="Interventions for preventing obesity in children")
    user2review3 = add_review(creator=user2,name="Interprofessional education: effects on professional practice and health care outcomes")
    #create queries
    create_query(user2review1,"((((((((((((((((((neuraminidase) AND antagonists and inhibitors) OR antagonists) AND inhibitors) OR antagonists and inhibitors) OR inhibitors) AND preventing) AND therapy) OR treating) AND influenza) human OR) influenza AND) human OR) human influenza OR) influenza AND) healthy AND) adult AND) child OR) children ")
    create_query(user2review2,"((((((((Interventions) AND preventing) AND pediatric obesity) OR pediatric) AND obesity) OR pediatric obesity) OR obesity) AND children) OR obesity in children")
    create_query(user2review3,"")

    #create 3rd user
    user3= add_user('jen')
    #add new user to list
    createdUsers.append(user3)
    #create reviews
    user3review1 = add_review(creator=user3,name="Interprofessional collaboration: effects of practice-based interventions on professional practice and healthcare outcomes")
    user3review2 = add_review(creator=user3,name="Risk assessment tools for the prevention of pressure ulcers")
    user3review3 = add_review(creator=user3,name="Midwife-led continuity models versus other models of care for childbearing women")
    #create queries
    create_query(user3review1,"(((((((((((((((((((((Interprofessional) AND cooperative behavior) OR cooperative) AND behavior) OR cooperative behavior) OR collaboration) AND effects) AND practice based) AND interventions) AND professional practice) OR professional practice) OR professional) AND practice) OR professional practice) AND delivery of health care) OR delivery) AND health) AND care) OR delivery of health care) OR healthcare) AND outcomes")
    create_query(user3review2,"(((((((((((((((((risk assessment) OR risk) AND assessment) OR risk assessment) AND tools) AND prevention and control) OR prevention) AND control) OR prevention and control) OR prevention) AND pressure ulcer) OR pressure) AND ulcer) OR pressure ulcer) OR pressure) AND ulcers) OR pressure ulcers")
    create_query(user3review3,"")

    # Print out what we have added to the users
    for createdUser in createdUsers:
        for review in Review.objects.filter(creator=createdUser):
            for query in Query.objects.filter(review=review):
                print "\nUser - {0}\nReview - {1}\nQuery - {2}".format(str(createdUser), str(review), str(query))

#create users
def add_user(username):
    #get or create new user
    user, created= User.objects.get_or_create(username=username)
    user.set_password(username)
    user.email = username + "@" + username +".com"
    user.save()
    #set up researcher profile
    researcher, created = Researcher.objects.get_or_create(user=user,name=username)
    researcher.surname = username
    researcher.bio = "This is "+ username +" bio."
    researcher.institution = "University of Glasgow"
    researcher.save()
    return user

#create reviews
def add_review(creator,name):
    #get or create new user
    review = Review.objects.get_or_create(creator=creator, name=name)[0]
    review.description = "This is a review on "+ name
    review.save()
    return review

#create queries
def create_query(review,queryString):
    query = Query.objects.get_or_create(review=review)[0]
    query.query_string = queryString
    query.save()
    return query

if __name__=='__main__':
    print "\nSysReview population script creates 3 users. Each user will have 3 reviews with the first 2 reviews containing a query.\n"
    time.sleep(1)
    print "Starting SysReview population script..."
    populate()
