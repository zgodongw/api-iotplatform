from django.urls import path
from api.views import *

# This is self explanatory really.

urlpatterns = [
    # Organisations
    path(
        'organisation/',
        OrganisationListApiView.as_view(),
        name='organisation'
        ),
    path(
        'organisation/add/',
        OrganisationCreateApiView.as_view(),
        name='add-organisation'
        ),
    path(
        'organisation/<str:name>/delete/',
        OrganisationDeleteApiView.as_view(),
        name='delete-organisation'
        ),

    # Sites
    path(
        'site/',
        SiteListApiView.as_view(),
        name='site'
        ),
    path(
        'site/add/',
        SiteCreateApiView.as_view(),
        name='add-site'
        ),
    path(
        'site/<str:place>/delete/',
        SiteDeleteApiView.as_view(),
        name='delete-site'
        ),

    # Assets
    path(
        'asset/',
        AssetListApiView.as_view(),
        name='asset'
        ),
    path(
        'asset/add/',
        AssetCreateApiView.as_view(),
        name='add-asset'
        ),
    path(
        'asset/<str:deviceID>/delete/',
        AssetDeleteApiView.as_view(),
        name='delete-asset'
        ),
    path(
        'asset/<str:deviceID>/update/',
        AssetUpdateApiView.as_view(),
        name='update-asset'
        ),

    # Activities
    path(
        'asset/activity/',
        ActivityListApiView.as_view(),
        name='activity'
        ),
    path(
        'asset/activity/add/',
        ActivityCreateApiView.as_view(),
        name='add-activity'
        )
]