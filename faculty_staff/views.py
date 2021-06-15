from django.shortcuts import redirect, render
from .models import Staff, StaffReview, IpModel
from django.views.generic import ListView, DetailView
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from django.db.models.functions import Lower
# Create your views here.

class StaffListView(ListView):
    model = Staff
    template_name = 'staff_list.html'
    context_object_name = 'staff_list'

    ordering = [Lower('last_name')]

    paginate_by = 50

def staff_post(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    staffReviewList = StaffReview.objects.filter(staff_name=staff)
    review_count = StaffReview.objects.filter(staff_name=staff).count()
    ip = get_client_ip(request)

    print("ip: %s" %ip)

    if not IpModel.objects.filter(ip=ip).exists():
        print("creating new ip")
        IpModel.objects.create(ip=ip)

    print("request method: ", request.method)

    if request.method == 'POST':

        #like_val = request.POST.get('like_btn')
        #dislike_val = request.POST.get('dislike_btn')

        print("in POST")

        print("request.POST: ", request.POST)

        if 'like_btn' in request.POST:
            #print("request POST: ", request.POST)
            #print(request.POST.get(id='staffreview'))
            #if request.POST.get('like_btn') == str(i.pk):
            like_val = request.POST.get('like_btn')
            the_staff = StaffReview.objects.filter(staff_name=staff, pk=int(like_val)).first()

            print("review pk: %d" %the_staff.pk)
            if not the_staff.likes.filter(id=IpModel.objects.get(ip=ip).id).exists() and \
                not the_staff.dislikes.filter(id=IpModel.objects.get(ip=ip).id).exists():
                the_staff.likes.add(IpModel.objects.get(ip=ip))
            #else:
            if the_staff.dislikes.filter(id=IpModel.objects.get(ip=ip).id).exists():
                #if ip exists in like
                print("exists in dislike")
                the_staff.likes.set(IpModel.objects.exclude(ip=ip))
                #i.likes.set(IpModel.objects.all())
            else:
                the_staff.likes.set(IpModel.objects.all())
        elif 'dislike_btn' in request.POST:
            print("in dislike")
            dislike_val = request.POST.get('dislike_btn')
            the_staff = StaffReview.objects.filter(staff_name=staff, pk=int(dislike_val)).first()

            #if request.POST.get('dislike_btn') == str(i.pk):
            if not the_staff.dislikes.filter(id=IpModel.objects.get(ip=ip).id).exists() and \
                not the_staff.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
                print("here")
                the_staff.dislikes.add(IpModel.objects.get(ip=ip))
            #else:
            if the_staff.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
                #if ip exists in like
                print("exists in like")
                the_staff.dislikes.set(IpModel.objects.exclude(ip=ip))
            else:
                the_staff.dislikes.set(IpModel.objects.all())
        
    return render(request, 'staffReview_list.html', \
            {
                'staffReviewList': staffReviewList, 
                'staff': staff, 
                'review_count': review_count, 
                'avg_exp': StaffReview.avg_experience(StaffReview, staffReviewList),
                #'likes': StaffReview.likes(StaffReview),
            })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip