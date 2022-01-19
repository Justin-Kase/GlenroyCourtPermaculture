import graphene
from graphene_django import DjangoObjectType
from .models import Report

class ReportType(DjangoObjectType):
    class Meta: 
        model = Report
        fields = ("ID","Temperature_Fahrenheit","Relative_Humidity","timestamp")

class Query(graphene.ObjectType):
    all_reports = graphene.List(ReportType)  

    def resolve_all_reports(root, info):
        return Report.objects.all()

schema = graphene.Schema(query=Query)