from django.shortcuts import render
from Departments.models import Department
from teachers.models import Teacher
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.
class DepartmentListView(ListView):
    model = Department
    template_name = 'dept_list.html' 
    context_object_name = 'department_list'

    def get_queryset(self):
        return Department.objects.order_by('dept_name')

def teachers_by_dept(request, dept_id):
    department = Department.objects.get(id=dept_id)
    #print(department)
    return render(request, 'teacherListByDept.html', \
        {'teacher_list': Teacher.objects.filter(dept__dept_abrv=department), 
        })

