from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


from . import serializers
from . import models

class LodgeDetailViewSet(viewsets.ModelViewSet):
    """Handles creating, deleting and updating Lodge Detail."""

    serializer_class = serializers.LodgeDetailSerializer
    queryset = models.LodgeDetail.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)