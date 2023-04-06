# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# This is our model for user registration.

class feedback(models.Model):
 ### The following are the fields of our table.
    username = models.CharField(max_length=255)
    product_id = models.CharField(max_length=10)
    feedback = models.CharField(max_length=200)
    rate = models.CharField(max_length=5)
    
    def __str__(self):
        return '%s %s %s %s' % (self.username, self.product_id, self.feedback, self.rate)