from django.shortcuts import render
from .models import Student

def page1(request):
    return render(request, 'page1.html')
def page2(request):
    students = Student.objects.all()  # fetch all students
    return render(request, 'page2.html', {'students': students})



