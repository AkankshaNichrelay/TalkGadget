from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from posts.models import Post
from django.core.urlresolvers import reverse_lazy
# Create your models here.
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

from django.contrib.auth import get_user_model
User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', related_name='post_comments')
    user = models.ForeignKey('auth.User', related_name='user_comments')
    text = models.TextField(default='')
    slug = models.SlugField(editable=False,default='', allow_unicode=True)
    created_date = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        logging.debug('This is called: get_absolute_url')
        return reverse_lazy("posts:post_detail", kwargs={'pk':self.post.pk})

    class Meta:
        ordering = ["-created_date"]
        unique_together = ["user","post","slug"]
