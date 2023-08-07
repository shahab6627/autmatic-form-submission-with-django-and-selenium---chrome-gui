from django.shortcuts import render
from .models import TestResult
import pandas as pd 
import xlrd
from django.contrib import messages
from .auto_form_submission import formSubmit
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get('patient_name')
        test_result = request.POST.get('test_result')
        gender = request.POST.get('gender')
        symptoms = request.POST.getlist('symptoms')
        all_sym = ""
        for symp in symptoms:
            all_sym += f'{symp},'

        add_test_result = TestResult.objects.create(patient_name = name, p_test_result = test_result,
        gender = gender, other_symptoms = all_sym[:-1]) # ll_sym[:-1] will remove the last comma
        add_test_result.save()
        messages.add_message(request, messages.SUCCESS, 'test added')
    return render(request, 'covid/index.html')

# autmate the form submission by submitting an excel file
def automateForm(request):
    if request.method == "POST":
        file_name = request.FILES['file_name']
        
        # print(ext)
        res = formSubmit(file_name)    
        return render(request, 'covid/automatform.html', {'res':res})
        
    return render(request, 'covid/automatform.html')



def testRecords(request):
    obj = TestResult.objects.all()
    
    return render(request, 'covid/tests_record.html', {'t_records':obj})