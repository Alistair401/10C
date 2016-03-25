from django.test import TestCase

from mainapp.models import Researcher, Review, Paper, Query
from django.contrib.auth.models import User


# tests for sysreviewer app models (only testing custom methods) - model testing tests for unicode returns and slug creation

# Researcher model testing
class ResearcherMethodTests(TestCase):

    #test unicode representation
    def test_unicode_researcher_representation(self):
        testUser=User(username = "bill")
        testUser.save()
        testResearcher = Researcher(user= testUser, name="bill", surname="bill")
        testResearcher.save()
        self.assertEqual(unicode(testResearcher), testResearcher.name)

# review model testing
class ReviewMethodTests(TestCase):

    #test unicode representation
    def test_unicode_Review_representation(self):
        testCreator=User(username="bill")
        testCreator.save()
        testReview = Review(creator=testCreator , name= "Test the review unicode")
        testReview.save()
        self.assertEqual(unicode(testReview), testReview.name)

    #test slug representation
    def test_slug_Review_representation(self):
        testCreator=User(username="bill")
        testCreator.save()
        testReview = Review(creator=testCreator, name= "Test the review slug")
        testReview.save()
        self.assertEqual(testReview.slug, "test-the-review-slug")

# query model testing
class QueryMethodTests(TestCase):

    #test unicode representation
    def test_unicode_query_representation(self):
        testCreator=User(username="bill")
        testCreator.save()
        testReview = Review(creator=testCreator, name= "Test Review for testing" )
        testReview.save()
        testQuery = Query(review=testReview,query_string="test the query unicode")
        testQuery.save()
        self.assertEqual(unicode(testQuery), testQuery.query_string)

#paper model test
class paperMethodTests(TestCase):

    #test unicode representation
    def test_unicode_paper_representation(self):
        testCreator=User(username="bill")
        testCreator.save()
        testReview = Review(creator=testCreator, name= "Test Review for testing" )
        testReview.save()
        testPaper = Paper(review=testReview,title="test the paper unicode")
        testPaper.save()
        self.assertEqual(unicode(testPaper), testPaper.title)

# class Paper(models.Model):
#
#
#     def test_unicode_representation(self):
#         testResearcher=Researcher(name="bill",surname="bill")
#         self.assertEqual(unicode(testResearcher), testResearcher.name)