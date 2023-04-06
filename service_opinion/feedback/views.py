from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import feedback as fb

### This function is inserting the feedback
def insert_feedback(uname, proid, feedb, rate):

    # Insert something
    feedback = fb(username = uname, product_id = proid,
                  feedback = feedb, rate = rate)
    feedback.save()

    return 1

    # pass

### This function will get the feedback from the front end.
@csrf_exempt
def send_feedback(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            uname = val1.get("User Name")
            proid = val1.get("Product Id")
            feedb = val1.get("Feedback")
            rate = val1.get("Rate")
            ### After all validation, it will call the data_insert function.
            if uname and proid and feedb and rate:
                respdata = insert_feedback(uname, proid, feedb, rate)
                ### If it returns value then will show success.
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'Feedback sent.'
                    ### If value is not found then it will give failed in response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Username or product ID does not exist.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Username or product ID does not exist.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

### This function is used for finding the feedback body.
def search_feedback(uname, proid):
    
    # Search
    data = fb.objects.filter(username = uname, product_id = proid)

    for val in data.values():
        return val
    
    # pass
    
### This function is used for getting the feedback
@csrf_exempt
def get_feedback(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            uname = variable1.get("User Name")
            proid = variable1.get("Product Id")
            ### It will call the shipment_data function.
            respdata = search_feedback(uname, proid)
            ### If it returns value then will show success.
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = respdata
        ### If it is not returning any value then it will show failed response.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Feedback data is not available.'
            print(uname, proid)
    return HttpResponse(json.dumps(resp), content_type = 'application/json')