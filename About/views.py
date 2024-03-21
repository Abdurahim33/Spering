from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from About.models import About_model, About_spering

class AboutView(ListView):
    template_name = 'about.html'


    def get_queryset(self) -> QuerySet[Any]:
        qs = About_model.objects.all()
        return qs
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['About'] = About_spering.objects.all()
        return data
    