from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from myapp.models import UserProfile
from myapp.serializers import UserSerializer


class ProfileAPI(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()

