from django.db import models
from django.db.models.fields import related

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name + ", " + self.first_name

    @property
    def get_review_count(self): 
        return StaffReview.objects.filter(staff_name=self).count()

class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class StaffReview(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 11)]

    staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    exp_rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    body = models.TextField()
    likes = models.ManyToManyField(IpModel, related_name="review_likes", blank=True)
    dislikes = models.ManyToManyField(IpModel, related_name="review_dislikes", blank=True)
    

    def avg_experience(self, reviews):
        avg = 0
        length = len(reviews)
        
        if length == 0:
            return 0

        for i in range(length):
            avg += reviews[i].exp_rating

        return ((avg/length) * 11)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()