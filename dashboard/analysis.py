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


from chartit import DataPool, Chart

def chart_view(request):
    context = RequestContext(request)
    #Step 1: Create a DataPool with the data we want to retrieve.
    visitdata = \
        DataPool(
           series=
            [{'options': {
               'source': Visit.objects.all()},
              'terms': [
                'visit_time',
                'type_of_visit']},
             {'options': {
               'source': BloodWork.objects.all()},
              'terms': [
                {'blood-date': 'date'},
                'reading']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = visitdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'visit_time': [
                    'type_of_visit'],
                'blood-date': ['reading']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Date of Visits'},
               'xAxis': {
                    'title': {
                       'text': 'Bwork'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('dashboard/analysis.html',{'chartview': cht}, context)