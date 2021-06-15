from django.shortcuts import render, get_object_or_404
from .models import IpPostModel, Teacher, Post
from faculty_staff.models import Staff
from django.views.generic import ListView, DetailView
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from .filters import PostFilter
from django.db.models.functions import Lower
from itertools import chain

# Create your views here.

#Lists all the teachers in the database
class TeacherListView(ListView):
    model = Teacher
    template_name = 'home.html'
    context_object_name = 'teacher_list'

    ordering = [Lower('last_name')]

    paginate_by = 50


class SearchResultsList(ListView):
    #model = Teacher
    template_name = 'search_results.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = []

        if query != "":
            try: 
                #search for classes ex: CHEM 124
                #does not work if input without space ex: CHEM124
                print("in try block")
                query_new = query.split(" ")
                int(query[-1])
                id_list = Post.objects.all().filter(
                    ~(~Q(classname__icontains=query_new[0]) | ~Q(classNumber__icontains=query_new[1]))
                ).values('teacher_name_id').distinct()
                object_list = Teacher.objects.filter(id__in=id_list)

                #print("id_list: ", id_list)
                #print("object_list", object_list)

            except:
                #print("in except block")
                teacher_list = Teacher.objects.filter(
                    Q(last_name__icontains=query) | 
                    Q(first_name__icontains=query) | 
                    Q(dept__dept_abrv__icontains=query) |
                    Q(dept__dept_name__icontains=query)
                )

                staff_list = Staff.objects.filter(
                    Q(last_name__icontains=query) |
                    Q(first_name__icontains=query)
                )

                object_list = chain(teacher_list, staff_list)

        return object_list

def teacher_post(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    review_list = Post.objects.filter(teacher_name=teacher).order_by('classname', 'classNumber')
    review_filter = PostFilter(request.GET, queryset=review_list)
    review_count = Post.objects.filter(teacher_name=teacher).count()

    ip = get_client_ip(request)

    print("ip: %s" %ip)

    if not IpPostModel.objects.filter(ip=ip).exists():
        print("creating new ip")
        IpPostModel.objects.create(ip=ip)

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
            the_prof = Post.objects.filter(teacher_name=teacher, pk=int(like_val)).first()

            print("review pk: %d" %the_prof.pk)
            if not the_prof.likes.filter(id=IpPostModel.objects.get(ip=ip).id).exists() and \
                not the_prof.dislikes.filter(id=IpPostModel.objects.get(ip=ip).id).exists():
                the_prof.likes.add(IpPostModel.objects.get(ip=ip))
            #else:
            if the_prof.dislikes.filter(id=IpPostModel.objects.get(ip=ip).id).exists():
                #if ip exists in like
                print("exists in dislike")
                the_prof.likes.set(IpPostModel.objects.exclude(ip=ip))
                #i.likes.set(IpModel.objects.all())
            else:
                the_prof.likes.set(IpPostModel.objects.all())
        elif 'dislike_btn' in request.POST:
            print("in dislike")
            dislike_val = request.POST.get('dislike_btn')
            the_prof = Post.objects.filter(teacher_name=teacher, pk=int(dislike_val)).first()

            #if request.POST.get('dislike_btn') == str(i.pk):
            if not the_prof.dislikes.filter(id=IpPostModel.objects.get(ip=ip).id).exists() and \
                not the_prof.likes.filter(id=IpPostModel.objects.get(ip=ip).id).exists():
                print("here")
                the_prof.dislikes.add(IpPostModel.objects.get(ip=ip))
            #else:
            if the_prof.likes.filter(id=IpPostModel.objects.get(ip=ip).id).exists():
                #if ip exists in like
                print("exists in like")
                the_prof.dislikes.set(IpPostModel.objects.exclude(ip=ip))
            else:
                the_prof.dislikes.set(IpPostModel.objects.all())


    return render(request, 'review_list.html', \
            {'review_list': review_list, 
            'teacher': teacher,
            'review_filter': review_filter, 
            'review_count': review_count,
            'avg_teaching': Post.avg_teaching(Post, review_list),
            'avg_difficulty': Post.avg_difficulty(Post, review_list)

             })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip