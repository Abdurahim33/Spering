from django.urls import path
from Category.views import CategoryView

app_name = 'Category'

urlpatterns = [
    path('Category/', CategoryView.as_view(), name='Category'),
]
