from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from posts.models import Post
from . import forms

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


from django.views.generic import (ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

## Edit previous comment

## Like a comment
@login_required
def comment_liked(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.like()
    return redirect('posts:post_detail', pk=comment.post.pk)

## dislike a comment
@login_required
def comment_disliked(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.dislike()
    return redirect('posts:post_detail', pk=comment.post.pk)

## delete a comment

## View a user's comments
class UserComments(ListView):
    model = Comment
    #template_name = "posts/user_comment_list.html"

    def get_queryset(self):
        try:
            return Comment.objects.filter(
                    author__username__iexact=self.kwargs.get("username")
                    ).order_by('-published_date')

        except User.DoesNotExist:
            raise Http404
        else:
            return redirect(reverse("home"))


## Add comment to post
class CreateCommentView(LoginRequiredMixin,CreateView):

    logging.debug('This is called.')
#    login_url = '/login.html/'
#    redirect_field_name = 'redirect_to'
    form_class = forms.CommentForm
    model = Comment

    def form_valid(self, form):
        form.instance.user = self.request.user
        current_post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        form.instance.post = current_post
        return super(CreateCommentView, self).form_valid(form)
