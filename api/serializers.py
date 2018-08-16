from rest_framework.serializers import ModelSerializer
from .models import *

# This takes data from your database and creates JSON data

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

class OrganisationCDUSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = [
            'name'
        ]

class SiteSerializer(ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class SiteCDUSerializer(ModelSerializer):
    class Meta:
        model = Site
        fields = [
            'place',
            'province',
            'organisation'
        ]

class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssetCDUSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'deviceName',
            'deviceID',
            'site',
            'location'
        ]

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityCDUSerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'asset',
            'datetime',
            'temperature',
            'vibrations',
            'cashAmount',
            'cashDeposits',
            'transactionSpeed',
            'humidity',
            'downloadSpeed',
            'paperLevel',
        ]