# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'text',
    )
