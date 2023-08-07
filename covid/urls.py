from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('upload-csv', automateForm, name="autoform-submit")
]