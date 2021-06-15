from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeacherListView.as_view(), name='home'),
    path('teacher/<int:teacher_id>/', views.teacher_post, name='review_list'),
    path('search/', views.SearchResultsList.as_view(), name='search_results'),
]