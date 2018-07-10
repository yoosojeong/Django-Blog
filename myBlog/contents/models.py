# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Content(TimeStampedModel):

    """ Content Model """

    title = models.TextField(max_length=30)
    text = models.TextField()
    tags =  TaggableManager()

class Comment():
    
    """ Comment Model """
    message = models.TextField()

class Like():
    
    """ Comment Model """
