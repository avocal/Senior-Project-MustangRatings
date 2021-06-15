from django.contrib import admin
from .models import Staff, StaffReview

# Register your models here.

class ReviewInLine(admin.StackedInline):
    model = StaffReview
    extra = 1

class StaffAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['last_name']}),
        (None,          {'fields': ['first_name']}),
        (None,          {'fields': ['title']}),
    ]
    inlines = [ReviewInLine]

admin.site.register(Staff, StaffAdmin)