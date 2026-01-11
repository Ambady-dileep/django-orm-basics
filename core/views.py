from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
# Create your views here.

def students_list(request):
    students = Student.objects.values()
    return JsonResponse(list(students),safe=False)
