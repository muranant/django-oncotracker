from django.shortcuts import render, render_to_response
from models import *
import random
from django.http import HttpResponse
import datetime
from django.views import generic
from django.template import Context, loader
from django.template.context import RequestContext
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    context = RequestContext(request)
    visit_list = Visit.objects.all()
    for v in visit_list:
        print v.visit_time
        print v.visit_time.date()
        #v.date = v.date.date()
    visit_dict = {'visits': visit_list}
    return render_to_response('dashboard/login.html', visit_dict, context)


def detail(request):
    print "MADEBUG"
    query_date = request.GET.get("date")
    print query_date
    context = RequestContext(request)
    query1 = Visit.objects.all()
    for visit in query1:
        print visit.visit_time
    print query1
    visit_dict = {'visits': query1}
    return render_to_response('dashboard/visit_details.html', visit_dict, context)


def analysis(request):
    template = loader.get_template('dashboard/analysis.html')
    context = Context({
    })
    return HttpResponse(template.render(context))

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Onco account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('dashboard/login.html', {}, context)
    
