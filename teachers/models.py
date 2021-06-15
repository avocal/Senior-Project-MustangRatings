from django.db import models
from Departments.models import Department
from django.core.validators import MinValueValidator

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, default=2)

    def __str__(self):
        return self.last_name + ", " + self.first_name

    @property
    def get_review_count(self): 
        return Post.objects.filter(teacher_name=self).count()

    class Meta:
        unique_together = ['first_name', 'last_name', 'dept']

class IpPostModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Post(models.Model):
    QUARTER_TAKEN = (
        ('Fall', 'Fall'),
        ('Winter', 'Winter'), 
        ('Spring', 'Spring'),
        ('Summer', 'Summer')
    )

    GRADE_CHOICES = (
        ('A', 'A'), 
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'), 
        ('B-', 'B-'),
        ('C+', 'C+'), 
        ('C', 'C'), 
        ('C-', 'C-'), 
        ('D', 'D'), 
        ('F', 'F'), 
        ('CREDIT', 'Credit'), 
        ('NO CREDIT', 'No Credit')
    )

    RATING_CHOICES = [(i, i) for i in range(1, 11)]


    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classname = models.CharField(max_length=5, null=True)
    classNumber = models.PositiveIntegerField(validators=[MinValueValidator(100)], null=True)
    quarter_taken = models.CharField(max_length=10, choices=QUARTER_TAKEN, null=True)
    year_taken = models.CharField(max_length=4, null=True)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, null=True)
    teaching_rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    difficulty_rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    body = models.TextField()
    likes = models.ManyToManyField(IpPostModel, related_name="review_likes", blank=True)
    dislikes = models.ManyToManyField(IpPostModel, related_name="review_dislikes", blank=True)

    def avg_teaching(self, reviews):
        avg = 0
        length = len(reviews)

        if length == 0:
            return 0

        for i in range(length):
            avg += reviews[i].teaching_rating

        '''
        print("len: ", length)
        print("avg: ", avg)
        print("avg / length: ", (avg/length))
        '''

        return ((avg/length) * 11)

    def avg_difficulty(self, reviews):
        avg = 0
        length = len(reviews)

        if length == 0:
            return 0

        for i in range(length):
            avg += reviews[i].difficulty_rating

        return ((avg/length) * 11)

    def total_likes(self):
            return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return str(self.teacher_name)