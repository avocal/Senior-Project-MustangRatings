from django.urls import path
from . import views


urlpatterns = [
    path('department-list/', views.DepartmentListView.as_view(), name='dept_list'), 
    path('department-list/professors/<int:dept_id>', views.teachers_by_dept, name='teacherListByDept')
]