from django.db import models

# Create your models here.
class TestResult(models.Model):
    patient_name = models.CharField(max_length=100)
    p_test_result = models.CharField(max_length=100)
    
    GENDER_CHOICES = (
        ('male','male'),
        ('female','female')
    )
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    
    other_symptoms = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.patient_name} - test result - {self.p_test_result}'