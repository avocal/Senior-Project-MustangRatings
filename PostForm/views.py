from django.shortcuts import render
from .forms import TeacherForm, ReviewForm, StaffReviewForm
from django.shortcuts import redirect
from teachers.models import Teacher, Post
from faculty_staff.models import StaffReview, Staff
from django.http import HttpResponseRedirect

# Create your views here.
def addNewAdmin(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid(): 
            post = form.save(commit=False)
            post.save()
            #return redirect('home')
            return redirect('review_list', teacher_id=post.pk)
    else: 
        form = TeacherForm()

    return render(request, 'addNewAdmin.html', {'form': form})


def newReviewPost(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    print("teacher id: %d" %teacher_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.teacher_name = teacher
            #post.teacher_name = Post.teacher_name
            post.save()
            return redirect('review_list', teacher_id=teacher_id)
    else: 
        form = ReviewForm()
    
    return render(request, 'newReviewPost.html', \
        {'form': form, 
        'teacher': teacher})


def newStaffReviewPost(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)

    if request.method == "POST":
        form = StaffReviewForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.staff_name = staff
            post.save()
            return redirect('staffReview_list', staff_id=staff_id)
    else:
        form = StaffReviewForm()

    return render(request, 'newStaffReviewPost.html', \
        {
            'form': form, 
            'staff': staff,
        })