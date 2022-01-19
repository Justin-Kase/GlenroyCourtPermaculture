import tempfile
from django.http import HttpResponse
from django.shortcuts import render
from .models import Report
from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


def index(request):
    greenhouse_data = Report.objects.all()
    #return HttpResponse('index.html')

    greenhouse_data_dict = {
        'greenhouse_data': greenhouse_data
    }

    return render(request, 'report.html', greenhouse_data_dict)

def report(request):
    greenhouse_data = Report.objects.all()

    greenhouse_data_dict = {
        'greenhouse_data': greenhouse_data
    }
    #return HttpResponse('index.html')
    return render(request, 'report.html', greenhouse_data_dict)     

def dashboard(request):
    greenhouse_data = Report.objects.all()

    greenhouse_data_dict = {
        'greenhouse_data': greenhouse_data
    }
    #return HttpResponse('index.html')
    return render(request, 'report.html', greenhouse_data_dict)          


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        ts    = Report.objects.values('timestamp')
        """Return 7 labels for the x-axis."""
        return [ts]

    def get_providers(self):
        """Return names of datasets."""
        return ["Temperature F", "Relative Humidity"]

    def get_data(self):
        """Return 2 datasets to plot."""
        tempF = Report.objects.values('Temperature_Fahrenheit')
        relH  = Report.objects.values('Relative_Humidity')
        
        return [[ tempF ],[ relH ]]


line_chart = TemplateView.as_view(template_name='chart.html')
line_chart_json = LineChartJSONView.as_view(template_name='chart.html') 