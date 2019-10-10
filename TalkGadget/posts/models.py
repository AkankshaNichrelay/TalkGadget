from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from accounts.models import UserProfile
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):

    REVIEWS = 'REVIEWS'
    GEAR = 'GEAR'
    GAMING = 'GAMING'
    ENTERTAINMENT = 'ENTERTAINMENT'
    CATEGORY_CHOICES = (
        (REVIEWS, 'Reviews'),
        (GEAR, 'Gear'),
        (GAMING, 'Gaming'),
        (ENTERTAINMENT, 'Entertainment'),
    )
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default=GEAR,
    )

    author = models.ForeignKey(User, related_name="posts")
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse_lazy("posts:post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
