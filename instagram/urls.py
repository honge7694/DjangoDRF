from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 URL을 만들어준다.
# router.urls # url pattern list


urlpatterns=[
    path('public/', views.PublicPostListAPIView.as_view()),
    path('', include(router.urls)),
]