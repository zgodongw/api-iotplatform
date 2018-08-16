from django.urls import path
from . import views

urlpatterns = [
    path(
        'register/',
        views.UserCreateApiView.as_view(),
        name='api-register'
        ),
    path(
        'user/',
        views.UserApiView.as_view()
        ),
     path(
        'user-only/',
        views.UserOnlyApiView.as_view()
        ),
    path(
        'profile/',
        views.UserProfileListApiView.as_view()
        ),
    path(
        'profile/create/',
        views.UserProfileCreateApiView.as_view()
        )
]