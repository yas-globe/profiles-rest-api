from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
from .views import HelloViewSet


router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='profiles_api_viewset')
router.register('profile', views.UserProfileViewSet, basename='profiles_api_profile-viewset')
router.register('feed', views.UserProfileFeedViewSet, basename='profiles_api_feed')

urlpatterns = [
    path('', include(router.urls), name='profiles_api_viewset'),
    path('login', views.UserLoginApiView.as_view(), name='profiles_api_login'),
    path('apiview/', views.HelloApiView.as_view(), name='profiles_api_apiview'),

]
