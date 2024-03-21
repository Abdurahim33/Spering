from django.urls import path
from Work.views import Work_view

app_name = 'Work'

urlpatterns = [
    path('Work/', Work_view.as_view(), name='Work'),
]

