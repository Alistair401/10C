from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from mainapp.forms import UserRegisterForm, UserProfileForm, CreateReviewForm, CreateAdvancedQuery
from mainapp.models import Researcher, Review, Query, Paper
from django.contrib.auth.models import User
from mainapp import pubmed
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.transaction import commit_on_success

KEYWORDS = ("AND ","OR ","NOT ")

#main home page
def index(request):
    user = request.user
    context_dict = {}
    current_review = None
    if user.is_authenticated:
        # Get the currently worked on review
        try:
            current_review = Researcher.objects.all().get_or_create(user=user)[0].selected_review
        except TypeError:
            pass
    context_dict["current_review"] = current_review
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

    # Get the currently worked on review
    current_review = current_profile.selected_review

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
                    'profile_institution':profile_institution,'current_review':current_review}
    return render(request,'mainapp/profile.html',context_dict)

#view saved reviews
def reviews(request):
    # Get the current user so that we can get the linked reviews
    current_user = request.user

    review_list = []
    # Get the linked reviews
    user_reviews = current_user.review_set.all()

    # Get the currently worked on review
    current_review = Researcher.objects.all().get(user=current_user).selected_review


    # If user_reviews isn't empty
    if user_reviews:
        # Loop through all the reviews
        for rev in user_reviews:
            # Get their name to pass to the context_dict
            review_list += [rev]
    context_dict = {'review_list':review_list,'current_review':current_review}

    return render(request,'mainapp/reviews.html',context_dict)

#page for selected review
@login_required
def review(request, review_name_slug):
    # Is this review currently being worked on?
    working = False
    deleted = False
    context_dict={}


    # The current user object
    current_user = request.user;

    # Get or create a UserProfile object for the user
    current_profile = Researcher.objects.all().get_or_create(user=current_user)[0]
    current_review = current_profile.selected_review

    # Try and get the review, fails if the review doesn't exist
    try:
        # Get the review from the slug
        slugged_review = Review.objects.get(slug=review_name_slug)


        # Save for good measure
        current_profile.save()

        # If the request is a POST
        if (request.method == 'POST'):
            if 'delete' in request.POST:
                if current_review == slugged_review.slug:
                    current_profile.selected_review=""
                slugged_review.delete()
                current_profile.save()
                current_review = ""
                deleted = True

        # If this review isn't being worked on
        if (current_profile.selected_review != slugged_review.slug):



                # If the POST was from the workon button
                if 'workon' in request.POST:

                    # Change the user's currently review to this one
                    current_profile.selected_review = slugged_review.slug
                    current_profile.save()
                    current_review = slugged_review.slug
                    working = True
        else:
            working = True

        context_dict['review_name']=slugged_review.name

        context_dict['review_description']=slugged_review.description

        context_dict['review_date_started']=slugged_review.date_started

        context_dict['pool_size']=slugged_review.pool_size

        context_dict['abstracts_judged']=slugged_review.abstracts_judged

        context_dict['document_judged']=slugged_review.document_judged

        context_dict['review'] = slugged_review

        context_dict['review_name_slug'] = review_name_slug

        context_dict['working'] = working





    except Review.DoesNotExist:
        pass

    context_dict['current_review'] = current_review
    context_dict['deleted'] = deleted
    return render(request, 'mainapp/review.html', context_dict)

#created new reviews
@login_required
def create_review(request):
    created = False
    failure = False
    current_user = request.user
    current_review = Researcher.objects.all().get_or_create(user=request.user)[0].selected_review
    if (request.method == 'POST'):
        review_form = CreateReviewForm(request.POST)
        if review_form.is_valid:
            entered_name = request.POST.get('name').upper()
            entered_description = request.POST.get('description')
            if not Review.objects.all().filter(name=entered_name):
                created_review = Review.objects.create(creator=current_user,name=entered_name,description=entered_description)
                created_review.save()
                created = True
            else:
                failure = True;
    else:
        review_form = CreateReviewForm()

    context_dict = {'review_form':review_form,'created':created,'failure':failure,'current_review':current_review}
    return render(request,'mainapp/create_review.html',context_dict)

#view saved queries
@login_required
def queries(request, review_name_slug):
    current_review = Researcher.objects.all().get_or_create(user=request.user)[0].selected_review
    review = Review.objects.get(slug=review_name_slug)
    queries = Query.objects.filter(review=review)
    queryList =[]
    # for query in queries:
    #     queryWords=query.query_string.split()
    #     tempString="("
    #     for word in queryWords:
    #         if word == 'AND':
    #             tempString=tempString[:-1]
    #             tempString+=") AND ("
    #         elif word == 'NOT':
    #             tempString=tempString[:-1]
    #             tempString+=") NOT ("
    #         else:
    #             tempString+=word+" "
    #     tempString=tempString[:-1]
    #     tempString+=")"
    #     queryList+=[tempString]

    context_dict = {'review_name_slug': review_name_slug,'queries':queries,'review':review,'queryList':queryList,'current_review':current_review}
    return render(request,'mainapp/queries.html',context_dict)

#create new query
@login_required
def create_query(request, review_name_slug):
    current_review = Researcher.objects.all().get_or_create(user=request.user)[0].selected_review
    context_dict = {'review_name_slug': review_name_slug,'current_review':current_review}
    return render(request,'mainapp/create_query.html', context_dict)

# view abstract pool and authorise abstracts and add to document pool
@login_required
def abstract_pool(request,review_name_slug):
    context_dict = {}
    current_review = Researcher.objects.all().get_or_create(user=request.user)[0].selected_review
    review = Review.objects.get(slug=review_name_slug)
    paper_list = Paper.objects.filter(review=review, abstract_relevance = False, document_relevance = False).order_by('title')
    context_dict = {'papers':paper_list, 'review_name':review.name,'current_review':current_review}
    return render(request,'mainapp/abstract_pool.html',context_dict)

# view document pool and authorise documents and add to final pool
@login_required
def document_pool(request,review_name_slug):
    context_dict = {}
    current_review = Researcher.objects.all().get_or_create(user=request.user)[0].selected_review
    review = Review.objects.get(slug=review_name_slug)
    paper_list = Paper.objects.filter(review=review, abstract_relevance = True, document_relevance = False).order_by('title')
    context_dict = {'review_name':review.name, 'papers':paper_list,'current_review':current_review}
    return render(request,'mainapp/document_pool.html',context_dict)

#view final pool and edit final pool
@login_required
def final_pool(request,review_name_slug):
    current_review = Researcher.objects.all().get_or_create(user=request.user)[0].selected_review
    context_dict = {}
    review = Review.objects.get(slug=review_name_slug)
    paper_list = Paper.objects.filter(review=review, abstract_relevance = True, document_relevance = True).order_by('title')
    context_dict = {'review_name':review.name, 'papers':paper_list,'current_review':current_review}
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
                # Get the user's associated profile or create on if none exist
                current_profile = Researcher.objects.all().get_or_create(user=user)[0]
                # Save for good measure
                current_profile.save()
                # set default review_name_slug
                current_profile.selected_review = None
    else:
        # Show the registration form to the user
        user_form = UserRegisterForm()
    context_dict = {'user_form': user_form,'registered':registered,'invalid':invalid,"review_name_slug":None}
    return render(request,'mainapp/userforms.html',context_dict)

#view to logout
#being logged in is required
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/mainapp/')

#view for deleting queries
def delete_query(request, review_name_slug,id):
    Query.objects.filter(pk=id).delete();
    return HttpResponse()

def check_API_adv(request,review_name_slug,query_string):
    # get list of ID results from PubMed API
    formatted = format_query_advanced(query_string)
    id_list = pubmed.esearch_query(formatted)
    return HttpResponse(len(id_list))

def check_API_std(request,review_name_slug,query_string):
    # get list of ID results from the PubMed API
    formatted = format_query_novice(query_string)
    id_list = pubmed.esearch_query(formatted)
    return HttpResponse(len(id_list))

def format_query_advanced(query_string):
    query_list = []
    query_lines = query_string.split(",")
    for unformatted_line in query_lines:
        line = unformatted_line.strip("\n")
        keyword_line=False
        for keyword in KEYWORDS:
            if keyword in line:
                query_list = parseKeywords(line, query_list,keyword)
                keyword_line = True
                break
        if not keyword_line:
            query_list.append(line)
    while "-" in query_list:
        query_list.remove("-")
    formatted_string = ""
    for i in query_list:
        formatted_string += i + " "
    return formatted_string

def format_query_novice(query_string):
    # formats the string with brackets (may be redundant)
    query_list = query_string.split(",")
    # removes weird empty strings from the query
    while "" in query_list:
        query_list.remove("")
    # add brackets
    for i in range(0, len(query_list)-1,2):
        query_list[0] = "(" + query_list[0]
        query_list[i] = query_list[i] + ")"
    # turn list back into string
    proper_query = ""
    for i in query_list:
        proper_query += i + " "
    # get abstracts
    return proper_query

def parseKeywords(line,list,keyword):
    # formatting stuff TODO: comment more stuff
    limits = [0,0]
    line_as_list = line.split(" ")
    limits[0] = int(line_as_list[1])

    if " TO " in line:
        limits[1] = int(line_as_list[3])
    else:
        limits[1] = int(line_as_list[1])

    limits[0] -= 1
    limits[1] -= 1

    result = list
    for i in range(limits[0],limits[1]+1):
        if i == 0:
            result[i] = result[i] + ")"
        else:
            result[i] = keyword.strip(" ") + " " + result[i] + ")"
        result[0] = "(" + result[0]
    result.append("-")
    return result

@commit_on_success
def remove_from_ap(request, review_name_slug):
    pks = request.POST.get("removed_rows", None)
    list_pks = pks.split(",")
    paperCounter=0 #counter for number of papers judged

    for id in list_pks[:-1]:
        Paper.objects.filter(pk=id).delete()
        paperCounter= paperCounter + 1 #increase counter

    review = Review.objects.get(slug=review_name_slug)
    review.pool_size = review.pool_size - paperCounter #decrease pool size as these papers now not relevant
    review.save()
    return HttpResponse()

@commit_on_success
def add_to_dp(request, review_name_slug):
    pks = request.POST.get("removed_rows")
    list_pks = pks.split(",")
    paperCounter=0 #counter for number of papers judged

    for id in list_pks[:-1]:
        Paper.objects.filter(pk=id).update(abstract_relevance=True)
        paperCounter= paperCounter + 1 #increase counter

    review = Review.objects.get(slug=review_name_slug)
    review.pool_size = review.pool_size - paperCounter #decrease pool size as these papers now not releva
    review.abstracts_judged = review.abstracts_judged + paperCounter #record number of abstracts judged
    review.save()
    return HttpResponse()

@commit_on_success
def remove_from_dp(request, review_name_slug):
    pks = request.POST.get("removed_rows")
    list_pks = pks.split(",")
    paperCounter=0 #counter for number of papers judged

    for id in list_pks[:-1]:
        Paper.objects.filter(pk=id).update(abstract_relevance=False)
        paperCounter= paperCounter + 1 #increase counter

    review = Review.objects.get(slug=review_name_slug)
    review.abstracts_judged = review.abstracts_judged - paperCounter #decrease pool size as these papers now not relevant
    review.pool_size = review.pool_size + paperCounter
    review.save()

    return HttpResponse()

@commit_on_success
def add_to_fp(request, review_name_slug):
    pks = request.POST.get("removed_rows")
    list_pks = pks.split(",")
    paperCounter=0 #counter for number of papers judged

    for id in list_pks[:-1]:
        Paper.objects.filter(pk=id).update(document_relevance=True)
        paperCounter= paperCounter + 1 #increase counter

    review = Review.objects.get(slug=review_name_slug)
    review.document_judged = review.document_judged + paperCounter #record number of documents judged
    review.abstracts_judged = review.abstracts_judged - paperCounter #decrease pool size as these papers now not relevant
    review.save()

    return HttpResponse()

@commit_on_success
def remove_from_fp(request, review_name_slug):
    pks = request.POST.get("removed_rows")
    list_pks = pks.split(",")
    paperCounter = 0 #counter for number of papers judged

    for id in list_pks[:-1]:
        Paper.objects.filter(pk=id).update(document_relevance=False)
        paperCounter= paperCounter + 1 #increase counter

    review = Review.objects.get(slug=review_name_slug)
    review.document_judged = review.document_judged - paperCounter #record number of documents judged
    review.abstracts_judged = review.abstracts_judged + paperCounter #decrease pool size as these papers    review.save()
    review.save()
    return HttpResponse()

@commit_on_success
def save_to_pool_adv(request, review_name_slug, query_string):
    review = Review.objects.get(slug=review_name_slug)
    # get list of ID results from the PubMed API
    formatted = format_query_advanced(query_string)
    esearch_result = pubmed.esearch_query(formatted)
    efetch_dict = pubmed.efetch_query(esearch_result)
    for id, attributes in efetch_dict.iteritems():
        paper = Paper.objects.create(review=review,title=attributes["title"],authors=str(attributes["authors"]),abstract=attributes["abstract"])
        paper.save()
    id_string = ""
    for id in esearch_result:
        id_string += id + ","
    id_string = id_string[:-1]
    query_object = Query.objects.create(review=review,query_string=formatted,pool_size=len(esearch_result),results=id_string)
    #set Review pool size
    review.pool_size=len(esearch_result)
    review.save()
    return HttpResponse()

@commit_on_success
def save_to_pool_std(request, review_name_slug, query_string):
    review = Review.objects.get(slug=review_name_slug)
    # get list of ID results from the PubMed API
    formatted = format_query_novice(query_string)
    esearch_result = pubmed.esearch_query(formatted)
    efetch_dict = pubmed.efetch_query(esearch_result)
    for id, attributes in efetch_dict.iteritems():
        paper = Paper.objects.create(review=review,title=attributes["title"],authors=str(attributes["authors"]),abstract=attributes["abstract"])
        paper.save()
    id_string = ""
    for id in esearch_result:
        id_string += id + ","
    id_string = id_string[:-1]
    query_object = Query.objects.create(review=review,query_string=formatted,pool_size=len(esearch_result),results=id_string)
    #set Review pool size
    review.pool_size=len(esearch_result)
    review.save()
    return HttpResponse()

@commit_on_success
def save_query_adv(request, review_name_slug, query_string):
    review = Review.objects.get(slug=review_name_slug)
    # get list of ID results from the PubMed API
    formatted = format_query_advanced(query_string)
    esearch_result = pubmed.esearch_query(formatted)
    for id in esearch_result:
        esearch_result += id + ","
    id_string = esearch_result[:-1]
    query_object = Query.objects.create(review=review,query_string=formatted,pool_size=len(esearch_result),results=id_string)
    return HttpResponse()

@commit_on_success
def save_query_std(request, review_name_slug, query_string):
    review = Review.objects.get(slug=review_name_slug)
    # get list of ID results from the PubMed API
    formatted = format_query_novice(query_string)
    esearch_result = pubmed.esearch_query(formatted)
    id_string = ""
    for id in esearch_result:
        id_string += id + ","
    id_string = id_string[:-1]
    query_object = Query.objects.create(review=review,query_string=formatted,pool_size=len(esearch_result),results=id_string)
    return HttpResponse()