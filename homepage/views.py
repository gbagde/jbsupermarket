from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class DefaultPage(TemplateView):
    template_name = "in/en/default/html/default.htm"