from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from mainapp.forms import UserRegisterForm, UserProfileForm, CreateReviewForm, CreateAdvancedQuery, AbstractPoolForm
from mainapp.models import Researcher, Review, Query
from django.contrib.auth.models import User
from mainapp import pubmed

#main home page
def index(request):
    context_dict = {}
    return render(request, 'mainapp/index.html', context_dict)

#view profile and edit profile
@login_required
def profile(request):
    # Has the form just been saved?
    saved = False

    # The current user object
    current_user = request.user

    # Get the user's associated profile or create on if none exist
    current_profile = Researcher.objects.all().get_or_create(user=current_user)[0]

    # Save for good measure
    current_profile.save()

    # If the form is submitted
    if request.method == 'POST':

        # The form data
        profile_form = UserProfileForm(data=request.POST)

        # If the form is valid
        if profile_form.is_valid:

            # If the form's field wasn't left empty save it to the profile
            entered_name = request.POST.get('name')
            if (entered_name != ""):
                current_profile.name = entered_name

            entered_surname = request.POST.get('surname')
            if (entered_surname != ""):
                current_profile.surname = entered_surname

            entered_bio = request.POST.get('bio')
            if (entered_bio != ""):
                current_profile.bio = entered_bio

            entered_institution = request.POST.get('institution')
            if (entered_institution != ""):
                current_profile.institution = entered_institution

            # Saves the profile
            current_profile.save()

            # The profile has been saved and the html can now be rendered to reflect that
            saved = True
    else:
        # Create a new form
        profile_form = UserProfileForm()

    profile_name = current_profile.name
    profile_surname = current_profile.surname
    profile_bio = current_profile.bio
    profile_institution = current_profile.institution

    context_dict = {'profile_form':profile_form,'saved':saved,'profile_name':profile_name,
                    'profile_surname':profile_surname,'profile_bio':profile_bio,
                    'profile_institution':profile_institution}
    return render(request,'mainapp/profile.html',context_dict)

#view saved reviews
def reviews(request):
    # Get the current user so that we can get the linked reviews
    current_user = request.user

    review_list = []
    # Get the linked reviews
    user_reviews = current_user.review_set.all()

    # If user_reviews isn't empty
    if user_reviews:
        # Loop through all the reviews
        for rev in user_reviews:
            # Get their name to pass to the context_dict
            review_list += [rev]
    context_dict = {'review_list':review_list}

    return render(request,'mainapp/reviews.html',context_dict)

#page for selected review
@login_required
def review(request, review_name_slug):
    # Is this review currently being worked on?
    working = False
    context_dict={}

    # The current user object
    current_user = request.user;

    # Try and get the review, fails if the review doesn't exist
    try:
        # Get the review from the slug
        review = Review.objects.get(slug=review_name_slug)

        # Get or create a UserProfile object for the user
        current_profile = Researcher.objects.all().get_or_create(user=current_user)[0]

        # Save for good measure
        current_profile.save()

        # If this review isn't being worked on
        if (current_profile.selected_review != review.name):

            # If the request is a POST
            if (request.method == 'POST'):

                # If the POST was from the workon button
                if 'workon' in request.POST:

                    # Change the user's currently review to this one
                    current_profile.selected_review = review.name
                    current_profile.save()
                    working = True
        else:
            working = True

        context_dict['review_name']=review.name

        context_dict['review'] = review

        context_dict['review_name_slug'] = review_name_slug

        context_dict['working'] = working



    except Review.DoesNotExist:
        pass

    return render(request, 'mainapp/review.html', context_dict)

#created new reviews
@login_required
def create_review(request):
    created = False
    failure = False
    current_user = request.user
    if (request.method == 'POST'):
        review_form = CreateReviewForm(request.POST)
        if review_form.is_valid:
            entered_name = request.POST.get('name').upper()
            if not Review.objects.all().filter(name=entered_name):
                current_review = Review.objects.create(creator=current_user,name=entered_name)
                current_review.save()
                created = True
            else:
                failure = True;
    else:
        review_form = CreateReviewForm()

    context_dict = {'review_form':review_form,'created':created,'failure':failure}
    return render(request,'mainapp/create_review.html',context_dict)

#view saved queries
def queries(request, review_name_slug):
    context_dict = {}

    return render(request,'mainapp/queries.html',context_dict)

#create new query
@login_required
def create_query(request, review_name_slug):
    #has a query been submitted
    submitted = False

    #get review for saving to primary key
    review = Review.objects.get(slug=review_name_slug)


    if request.method == 'POST':
        #if advanced search submitted
        if 'advanced' in request.POST:
            advanced_query = CreateAdvancedQuery(data=request.POST)
            if advanced_query.is_valid():
                newQuery = request.POST.get('query_string') # get query submitted
                pubmed.query(newQuery)
                query = Query.objects.create(review=review, query_string=newQuery) #create new query and set primary key to review
                query.save()
                submitted=True #set query to submitted
    else:
        advanced_query = CreateAdvancedQuery()
    context_dict = {'review_name_slug': review_name_slug, 'advanced_query':advanced_query, 'submitted':submitted}
    return render(request,'mainapp/create_query.html', context_dict)

#view query results and authorise queries and add to abstract pool
def query_results(request):
    context_dict = {}

    return render(request,'mainapp/query_results.html',context_dict)

#view abstract pool and authorise abstracts and add to document pool
def abstract_pool(request,review_name_slug):
    context_dict = {}
    if request.method == 'POST':
        APForm = AbstractPoolForm(data=request.POST)
        if APForm.is_valid(): #If we have been provided with a valid form
            APForm.save(commit=True) #Save the abstract pool to the database
    else:
        APForm = AbstractPoolForm()
    context_dict = {'review_name_slug':review_name_slug, 'APForm':APForm}
    return render(request,'mainapp/abstract_pool.html',context_dict)

#view document pool and authorise documents and add to final pool
def document_pool(request,review_name_slug):
    context_dict = {}

    return render(request,'mainapp/document_pool.html',context_dict)

#view final pool and edit final pool
def final_pool(request,review_name_slug):
    context_dict = {}

    return render(request,'mainapp/final_pool.html',context_dict)

#view for the login / register page
def user_login(request):
    # If registration is successful registered = True
    registered = False
    invalid = False

    # If the view is accessed through POST
    if request.method == 'POST':
        user_form = UserRegisterForm()

        # If the login button is pressed
        if 'login' in request.POST:
            # Get the username and password entered in the form
            form_username = request.POST.get('username')
            form_password = request.POST.get('password')
            # Authenticate the user
            user = authenticate(username=form_username, password=form_password)
            # If the authentication is sucessful
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/mainapp/')
            else:
                # Bad login details were provided. So we can't log the user in.
                print "Invalid login details:{0},{1}".format(form_username,form_password)
                invalid = True

        # If the register button is pressed
        elif 'register' in request.POST:
            # Take data from form
            user_form = UserRegisterForm(data=request.POST)
            # If the form is valid
            if user_form.is_valid():
                # Save a new user
                user = user_form.save()
                user.save()
                # Hash the new user's password
                user.set_password(request.POST.get('password'))
                # Save the update
                user.save()
                # Registration was successful
                registered = True
        #else:
            # Print errors with the invalid form
            # print user_form.errors
    else:
        # Show the registration form to the user
        user_form = UserRegisterForm()
    context_dict = {'user_form': user_form,'registered':registered,'invalid':invalid}
    return render(request,'mainapp/userforms.html',context_dict)

#view to logout
#being logged in is required
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/mainapp/')
