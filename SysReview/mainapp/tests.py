from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.urlresolvers import reverse
from mainapp.forms import CreateReviewForm


from mainapp.models import Researcher, Review, Paper, Query
from django.contrib.auth.models import User


# tests for sysreviewer app models (only testing custom methods) - model testing tests for unicode returns and slug creation

# Researcher model testing
class ResearcherMethodTests(TestCase):

    #test unicode representation
    def test_unicode_researcher_representation(self):
        #create test user for foreign key
        testUser=User(username = "bill")
        testUser.save()
        #create test researcher
        testResearcher = Researcher(user= testUser, name="bill", surname="bill")
        testResearcher.save()
        #test
        self.assertEqual(unicode(testResearcher), testResearcher.name)

# review model testing
class ReviewMethodTests(TestCase):

    #test unicode representation
    def test_unicode_Review_representation(self):
        #create test user for foreign key
        testCreator=User(username="bill")
        testCreator.save()
        #create test review
        testReview = Review(creator=testCreator , name= "Test the review unicode")
        testReview.save()
        #test
        self.assertEqual(unicode(testReview), testReview.name)

    #test slug representation
    def test_slug_Review_representation(self):
        #create test user for foreign key
        testCreator=User(username="bill")
        testCreator.save()
        #create test review
        testReview = Review(creator=testCreator, name= "Test the review slug")
        testReview.save()
        #test
        self.assertEqual(testReview.slug, "test-the-review-slug")

# query model testing
class QueryMethodTests(TestCase):

    #test unicode representation
    def test_unicode_query_representation(self):
        #create test user for foreign key in review
        testCreator=User(username="bill")
        testCreator.save()
        #create test review for foreign key in query
        testReview = Review(creator=testCreator, name= "Test Review for testing" )
        testReview.save()
        #create test query
        testQuery = Query(review=testReview,query_string="test the query unicode")
        testQuery.save()
        #test
        self.assertEqual(unicode(testQuery), testQuery.query_string)

#paper model test
class paperMethodTests(TestCase):

    #test unicode representation
    def test_unicode_paper_representation(self):
        #create test user for foreign key in review
        testCreator=User(username="bill")
        testCreator.save()
        #create test review for foreign key in paper
        testReview = Review(creator=testCreator, name= "Test Review for testing" )
        testReview.save()
        #create paper
        testPaper = Paper(review=testReview,title="test the paper unicode")
        testPaper.save()
        #test
        self.assertEqual(unicode(testPaper), testPaper.title)

# testing views

#test index view
class IndexViewTests(TestCase):

    #set up test user
    def setUp(self):
        user = User.objects.create_user(username='bill', email='bill@bill.com', password='bill')

    # test index content with no user logged in
    def test_index_view_with_no_login(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to SysReviewer - The Systematic Review App")

    #test when user logged in
    def test_index_view_with_login(self):
        self.client.login(username='bill', password='bill')
        response = self.client.get(reverse('index'), follow=True)
        user = User.objects.get(username='bill')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You aren't working on any reviews")
        self.assertEqual(response.context['user'], user)

#test CreateReviewForm form
class CreateReviewFormTests(TestCase):

    def test_valid_form(self):
        #create test data
        data = {'name': 'test the form', 'description':'test the form',}
        #create form
        form = CreateReviewForm(data=data)
        #check form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        #create test incorrect data
        data = {'name': '', 'description':'test the form',}
        #create form
        form = CreateReviewForm(data=data)
        #check form is not valid
        self.assertFalse(form.is_valid())













































































