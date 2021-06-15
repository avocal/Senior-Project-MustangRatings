from django import forms
from teachers.models import Teacher, Post
from faculty_staff.models import StaffReview
from Departments.models import Department
from django import apps

class TeacherForm(forms.ModelForm):
    class Meta: 
        model = Teacher
        fields = {'first_name', 'last_name', 'dept'}

        labels = {
            'dept': 'Department'
        }

    field_order = ['first_name', 'last_name', 'dept']

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

        for key in self.fields: 
            self.fields[key].required = True


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'classname', 'classNumber', 'grade', 'quarter_taken', 'year_taken', 'teaching_rating', 'difficulty_rating', 'body'}

        labels = {
            'classname': 'Course', 
            'classNumber' : 'Course Number',
            'quarter_taken': 'Quarter Taken',
            'year_taken': 'Year', 
            'grade': 'Grade Received', 
            'teaching_rating': 'Teaching Rating', 
            'difficulty_rating': 'Difficulty Rating'
        }

    field_order = ['classname', 'classNumber', 'quarter_taken', 'year_taken', 'grade', 'teaching_rating', 'difficulty_rating', 'body']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for key in self.fields: 
            self.fields[key].required = True


class StaffReviewForm(forms.ModelForm):
    class Meta:
        model = StaffReview
        fields = {'exp_rating', 'body'}

        labels = {
            'exp_rating': 'Experience Rating',
        }

        field_order = ['exp_rating', 'body']

        def __init__(self, *args, **kwargs):
            super(StaffReviewForm, self).__init__(*args, **kwargs)

            for key in self.fields:
                self.fields[key].required = True