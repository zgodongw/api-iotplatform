from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

# View are what you put in and get back
# Organisations {

class OrganisationListApiView(ListAPIView):
    serializer_class = OrganisationSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Organisation.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
                ).distinct()
        return queryset_list

class OrganisationCreateApiView(CreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationCDUSerializer

class OrganisationDeleteApiView(DestroyAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationCDUSerializer
    lookup_field = 'name'

# }



# Sites {

class SiteListApiView(ListAPIView):
    serializer_class = SiteSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Site.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(place__icontains=query) |
                Q(organisation__name__icontains=query)
                ).distinct()
        return queryset_list

class SiteCreateApiView(CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteCDUSerializer

class SiteDeleteApiView(DestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteCDUSerializer
    lookup_field = 'place'

# }



# Assets {

class AssetListApiView(ListAPIView):
    serializer_class = AssetSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Asset.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(deviceID__icontains=query) |
                Q(site__place__icontains=query)
                ).distinct()
        return queryset_list

class AssetCreateApiView(CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetCDUSerializer

class AssetDeleteApiView(DestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetCDUSerializer
    lookup_field = 'deviceID'

class AssetUpdateApiView(UpdateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetCDUSerializer
    lookup_field = 'deviceID'

# }



# Activitys {    

class ActivityListApiView(ListAPIView):
    serializer_class = ActivitySerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Activity.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(asset__deviceID__icontains=query)
                ).distinct()
        return queryset_list

class ActivityCreateApiView(CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivityCDUSerializer
    permission_classes = [AllowAny]

# }

# Site destroy had a problem
# Asset destroy had a problem

    
    