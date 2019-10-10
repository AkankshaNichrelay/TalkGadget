from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from braces.views import SelectRelatedMixin
from django.views.generic import (ListView,
                        UpdateView, DeleteView,
                        CreateView, DetailView)

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

## List all posts
class PostListView(SelectRelatedMixin, ListView):
    model = models.Post
    select_related = ("author",)

    def get_queryset(self):
        return models.Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


## List a user's posts
class UserPosts(ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            return models.Post.objects.filter(
            author__username__iexact=self.kwargs.get("username")).filter(
            published_date__lte=timezone.now()).order_by('-published_date')

        except User.DoesNotExist:
            raise Http404
        else:
            return redirect(reverse("posts:all"))


## Post detail page
class PostDetailView(SelectRelatedMixin, DetailView):
    model = models.Post
    select_related = ("author",)
    template_name = 'posts/post_detail.html'


## Create post
class CreatePostView(LoginRequiredMixin,CreateView):

    login_url = '/login/'
    fields = ('author','title', 'text', 'category',)
    model = models.Post

## Update post
class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    fields = ('title', 'text', 'category',)
    model = models.Post

## Delete post

## Draft List
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_draft_list.html'

    model = models.Post

    def get_queryset(self):
        try:
            return models.Post.objects.filter(
            author__username__iexact=self.kwargs.get("username")).filter(
            published_date__isnull=True).order_by('created_date')

        except User.DoesNotExist:
            raise Http404
        else:
            return redirect(reverse("posts:all"))

## Saved Post list

## Category Post List

## Shares

## Publish post
@login_required
def post_publish(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    return redirect('posts:post_detail', pk=pk)
