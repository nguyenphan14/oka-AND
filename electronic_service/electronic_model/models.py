# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# This is our model for user registration.
class elec_details(models.Model):
    ### The following are the fields of our table.
    product_id = models.CharField(max_length=10)
    elec_category = models.CharField(max_length=50)
    elec_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s' % (self.product_id, self. elec_category,self.elec_name, self.availability, self.price)
