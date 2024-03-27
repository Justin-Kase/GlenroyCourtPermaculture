from django.urls import path
from graphql import graphql
from . import views
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from dashboard.schema import schema

urlpatterns = [
    path('/vegetables', views.vegetables, name='vegetables'),
]