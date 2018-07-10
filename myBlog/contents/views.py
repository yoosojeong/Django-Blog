# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from contents import models
from contents import serializers 

class Contents(APIView):

    def get(self, request, foramt=None):

        show_contents = models.Content.objects.get()

        serializer = serializers.ContentSerializer(show_contents)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

        
