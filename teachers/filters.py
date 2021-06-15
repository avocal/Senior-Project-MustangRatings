import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    year_range_start = django_filters.NumberFilter(field_name='year_taken', label='Year From', lookup_expr='gte')
    year_range_end = django_filters.NumberFilter(field_name='year_taken', label='To', lookup_expr='lte')
    class_name = Post.objects.distinct('classname')
    class Meta: 
        model = Post
        fields = ['classname', 'classNumber', 'year_range_start', 'year_range_end']