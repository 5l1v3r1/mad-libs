from django.shortcuts import render
from django.views.generic import TemplateView
import subprocess

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class RomanticPoetryView(TemplateView):
    template_name = "romantic_poetry.html"

    def post(self, request, **kwargs):
        line1 = "Roses are " + request.POST.get('adj1', None).lower()
        line2 = request.POST.get('noun1', None).title() + " are blue"
        line3 = request.POST.get('noun2', None).title() + " is " + request.POST.get('adj2', None).lower()
        data = {'line1': line1, 'line2': line2, 'line3': line3, 'line4': "And so are you!"}
        return render(request, 'result.html', data)

class ResultsPageView(TemplateView):
    def get(self, request, **kwargs):
        data = kwargs['data']
        return render(request, 'result.html', data)
