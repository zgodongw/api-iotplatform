from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.MessageListAPIView.as_view(),
        name='message'
        ),
    path(
        'add/',
        views.MessageCreateAPIView.as_view(),
        name='message-add'
        )
]