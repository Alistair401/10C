from django.shortcuts import render

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