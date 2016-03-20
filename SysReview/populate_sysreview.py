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
    create_query(user1review1,"Interventions[All Fields] AND preventing[All Fields] AND (accidental falls[MeSH Terms] OR (accidental[All Fields] AND falls[All Fields]) OR accidental falls[All Fields] OR falls[All Fields]) AND older[All Fields] AND (persons[MeSH Terms] OR persons[All Fields] OR people[All Fields]) AND (life[MeSH Terms] OR life[All Fields] OR living[All Fields]) AND (residence characteristics[MeSH Terms] OR (residence[All Fields] AND characteristics[All Fields]) OR residence characteristics[All Fields] OR community[All Fields])")
    create_query(user1review2,"(exercise[MeSH Terms] OR exercise[All Fields]) AND (depressive disorder[MeSH Terms] OR (depressive[All Fields] AND disorder[All Fields]) OR depressive disorder[All Fields] OR depression[All Fields] OR depression[MeSH Terms])")
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
    create_query(user2review1,"(neuraminidase[MeSH Terms] OR neuraminidase[All Fields]) AND (antagonists and inhibitors[Subheading] OR (antagonists[All Fields] AND inhibitors[All Fields]) OR antagonists and inhibitors[All Fields] OR inhibitors[All Fields]) AND preventing[All Fields] AND (therapy[Subheading] OR therapy[All Fields] OR treating[All Fields]) AND (influenza, human[MeSH Terms] OR (influenza[All Fields] AND human[All Fields]) OR human influenza[All Fields] OR influenza[All Fields]) AND healthy[All Fields] AND (adult[MeSH Terms] OR adult[All Fields] OR adults[All Fields]) AND (child[MeSH Terms] OR child[All Fields] OR children[All Fields])")
    create_query(user2review2,"Interventions[All Fields] AND preventing[All Fields] AND (pediatric obesity[MeSH Terms] OR (pediatric[All Fields] AND obesity[All Fields]) OR pediatric obesity[All Fields] OR (obesity[All Fields] AND children[All Fields]) OR obesity in children[All Fields])")
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
    create_query(user3review1,"(Interprofessional[All Fields] AND (cooperative behavior[MeSH Terms] OR (cooperative[All Fields] AND behavior[All Fields]) OR cooperative behavior[All Fields] OR collaboration[All Fields])) AND (effects[All Fields] AND practice-based[All Fields] AND interventions[All Fields] AND (professional practice[MeSH Terms] OR (professional[All Fields] AND practice[All Fields]) OR professional practice[All Fields]) AND (delivery of health care[MeSH Terms] OR (delivery[All Fields] AND health[All Fields] AND care[All Fields]) OR delivery of health care[All Fields] OR healthcare[All Fields]) AND outcomes[All Fields])")
    create_query(user3review2,"(risk assessment[MeSH Terms] OR (risk[All Fields] AND assessment[All Fields]) OR risk assessment[All Fields]) AND tools[All Fields] AND (prevention and control[Subheading] OR (prevention[All Fields] AND control[All Fields]) OR prevention and control[All Fields] OR prevention[All Fields]) AND (pressure ulcer[MeSH Terms] OR (pressure[All Fields] AND ulcer[All Fields]) OR pressure ulcer[All Fields] OR (pressure[All Fields] AND ulcers[All Fields]) OR pressure ulcers[All Fields])")
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
