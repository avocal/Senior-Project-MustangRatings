from django.contrib import admin
from .models import Teacher, Post

# Register your models here.

class PostInLine(admin.StackedInline):
    model = Post
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['last_name']}),
        (None,          {'fields': ['first_name']}),
        (None,          {'fields': ['dept']}),
    ]
    inlines = [PostInLine]

admin.site.register(Teacher, TeacherAdmin)
#admin.site.register(Teacher)
#admin.site.register(Department)
#admin.site.register(Post)