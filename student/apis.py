#this file is for handling django rest framework part
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .models import Blogs
from .serializers import BlogSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
class BlogViewSet(ModelViewSet):
    serializer_class=BlogSerializer
    queryset=Blogs.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]