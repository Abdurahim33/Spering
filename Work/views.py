from django.shortcuts import render
from django.views.generic import ListView
from Work.models import Work_model

class Work_view(ListView):
    model = Work_model
    template_name = 'work.html'