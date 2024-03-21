from django.shortcuts import render
from django.views.generic import ListView
from Category.models import Category_model

class CategoryView(ListView):
    model = Category_model
    template_name = 'category.html'