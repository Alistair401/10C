import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SysReview.settings')

import django
django.setup()

from mainapp.models import Review, Paper, Query, Researcher
from django.contrib.auth.models import User


def populate():
    user1= add_user(username='jill')
    add_review(user=user1,name="Effects of diabetes")

def add_user(username):
    user = User.objects.get_or_create(username=username)[0]
    user.set_password(username)
    user.email = username + "@" + username +".com"
    user_profile = Researcher.objects.all().get_or_create(user=user)[0]
    user_profile.name = username
    user_profile.surname = username
    user_profile.bio = "This is "+ username +" bio."
    user_profile.institution = "University of Glasgow"
    user.save()
    user_profile.save()



if __name__=='__main__':
    print "Starting SysReview population script..."
    populate()