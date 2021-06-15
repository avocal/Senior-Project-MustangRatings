from django.urls import path
from . import views

urlpatterns = [
    path('staff-administrator/', views.StaffListView.as_view(), name='staff_list'), 
    path('staff-administrator/<int:staff_id>/', views.staff_post, name='staffReview_list'),
]
