from django.conf.urls import url

from . import views

app_name='posts'

urlpatterns = [
    url(r"^$", views.PostListView.as_view(), name="all"),
    url(r"new/$", views.CreatePostView.as_view(), name="create"),
    url(r"(?P<pk>\d+)/edit/$", views.UpdatePostView.as_view(), name="post_edit"),
    url(r"(?P<pk>\d+)/detail/$",views.PostDetailView.as_view(),name="post_detail"),
    url(r'(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="user_post_list"),
    url(r'^drafts/(?P<username>[-\w]+)/$', views.DraftListView.as_view(), name='post_draft_list'),
    # url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
    # url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
]
