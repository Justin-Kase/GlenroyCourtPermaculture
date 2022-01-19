from django.urls import path
from graphql import graphql
from . import views
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from dashboard.schema import schema
from dashboard.views import line_chart, line_chart_json


urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]