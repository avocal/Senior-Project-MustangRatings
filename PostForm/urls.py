from django.urls import path
from . import views


urlpatterns = [
    path('post/new-admin/', views.addNewAdmin, name='addNewAdmin'), 
    path('teacher/new-review/<int:teacher_id>/', views.newReviewPost, name='newReviewPost'),
    path('staff-administrator/new-review/<int:staff_id>/', views.newStaffReviewPost, name='newStaffReviewPost'),
]