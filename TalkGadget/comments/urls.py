from django.conf.urls import url

from . import views

app_name='comments'

urlpatterns = [
    #url(r"^$", views.PostListView.as_view(), name="all"),
    url(r"for/(?P<post_pk>\d+)/new/$", views.CreateCommentView.as_view(), name="create"),
    # url(r"(?P<pk>\d+)/edit/$", views.UpdatePostView.as_view(), name="post_edit"),
    # url(r"(?P<pk>\d+)/detail/$",views.PostDetailView.as_view(),name="post_detail"),
    url(r'^comment/(?P<pk>\d+)/like/$', views.comment_liked, name='comment_liked'),
    url(r'^comment/(?P<pk>\d+)/dislike/$', views.comment_disliked, name='comment_disliked'),
    url(r"by/(?P<username>[-\w]+)/$",views.UserComments.as_view(),name="user_comment_list"),
]
