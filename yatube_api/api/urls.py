from rest_framework import routers
from django.urls import include, path


from posts.views import (PostViewSet, GroupViewSet,
                         CommentViewSet, FollowViewSet)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comment')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
]
