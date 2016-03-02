from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from mainapp.forms import UserRegisterForm, UserLoginForm

#main home page
def index(request):
    context_dict = {}
    return render(request, 'mainapp/index.html', context_dict)

#view profile and edit profile
def profile(request):
    context_dict = {}
    return render(request,'mainapp/profile.html',context_dict)

#view saved reviews
def reviews(request):
    context_dict = {}

    return render(request,'mainapp/reviews.html',context_dict)

#created new reviews
def create_review(request):
    context_dict = {}

    return render(request,'mainapp/create_review.html',context_dict)

#view saved queries
def queries(request):
    context_dict = {}

    return render(request,'mainapp/queries.html',context_dict)

#create new query
def create_query(request):
    context_dict = {}

    return render(request,'mainapp/create_query.html',context_dict)

#view query results and authorise queries and add to abstract pool
def query_results(request):
    context_dict = {}

    return render(request,'mainapp/query_results.html',context_dict)

#view abstract pool and authorise abstracts and add to document pool
def abstract_pool(request):
    context_dict = {}

    return render(request,'mainapp/abstract_pool.html',context_dict)

#view document pool and authorise documents and add to final pool
def document_pool(request):
    context_dict = {}

    return render(request,'mainapp/document_pool.html',context_dict)

#view final pool and edit final pool
def final_pool(request):
    context_dict = {}

    return render(request,'mainapp/final_pool.html',context_dict)

#view for the login / register page
def user_login(request):
    # If registration is successful registered = True
    registered = False
    loggedIn = False

    # If the view is accessed through POST
    if request.method == 'POST':
        # If the login button is pressed
        if 'login' in request.POST:
            # Take the data from the form
            user_form = UserLoginForm(data=request.POST)
            if user_form.is_valid():
                # Get the username and password entered in the form
                username = request.POST.get('username')
                password = request.POST.get('password')
                # Authenticate the user
                user = authenticate(username=username, password=password)
                # If the authentication is sucessful
                if user:
                    login(request, user)
                    return HttpResponseRedirect('/mainapp/')
                else:
                    # Bad login details were provided. So we can't log the user in.
                    print "Invalid login details: {0}, {1}".format(username, password)
                    return HttpResponse("Invalid login details supplied.")

        # If the register button is pressed
        else:
            # Take data from form
            user_form = UserRegisterForm(data=request.POST)
            # If the form is valid
            if user_form.is_valid():
                # Save a new user
                user = user_form.save()
                # Update the new user's password
                user.set_password(user.password)
                # Save the update
                user.save
                # Registration was successful
                registered = True
        #else:
            # Print errors with the invalid form
            # print user_form.errors
    else:
        # Show the registration form to the user
        user_form = UserRegisterForm()
        login_form = UserLoginForm()
    context_dict = {'user_form': user_form,'registered':registered,'login_form':login_form}
    return render(request,'mainapp/userforms.html',context_dict)

#view to logout
#being logged in is required
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/mainapp/')
