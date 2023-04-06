from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Cart, Item

def insert_item(uname, proid, quant):

    newcart = None
    for val in Cart.objects.filter(username = uname).all():
        newcart = val
    if newcart == None:
        newcart = Cart(username = uname)
        newcart.save()

    if newcart.cart.filter(product_id = proid).count() == 0:
        newcart.cart.create(product_id = proid, quantity = quant)
    else:
        lst = newcart.cart.all()
        for x in lst:
            if x.product_id == proid:
                newcart.cart.remove(x)
                x.quantity += str(int(x.quantity) + int(quant))
                newcart.cart.add(x)
                break
    
    newcart.save()
    return 1

@csrf_exempt
def add_item(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            uname = val1.get("User Name")
            proid = val1.get("Product Id")
            quant = val1.get("Quantity")
            ### After all validation, it will call the data_insert function.
            if uname and proid and quant:
                respdata = insert_item(uname, proid, quant)
                ### If it returns value then will show success.
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'Feedback sent.'
                    ### If value is not found then it will give failed in response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '401'
                    resp['message'] = 'Username or product ID does not exist.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Username or product ID does not exist.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

def get_item(uname):

    cart = Cart.objects.filter(username = uname).all()
    # print(cart)

    # for val in cart.values():
    #     return val

    for val in cart.all():
        print(val)
        ret = {}
        for item in val.cart.all():
            ret[item.product_id] = item.quantity
        print(ret)
        return ret

@csrf_exempt
def show_cart(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            uname = variable1.get("User Name")
            ### It will call the shipment_data function.
            respdata = get_item(uname)
            ### If it returns value then will show success.
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = respdata
        ### If it is not returning any value then it will show failed response.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Cart is not available.'
            print(uname)
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

def clear_cart(uname):
    cart = Cart.objects.filter(username = uname).all()

    for val in cart:
        val.delete()
    
    return 1

@csrf_exempt
def delete_cart(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            uname = variable1.get("User Name")
            ### It will call the shipment_data function.
            respdata = clear_cart(uname)
            ### If it returns value then will show success.
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = respdata
        ### If it is not returning any value then it will show failed response.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Cart is not available.'
            print(uname)
    return HttpResponse(json.dumps(resp), content_type = 'application/json')