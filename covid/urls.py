from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('automatic-form', automateForm, name="autoform-submit"),
    path('all-test', testRecords, name="test-records")
]