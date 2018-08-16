from django.contrib import admin
from .models import (
    Organisation,
    Site,
    Asset,
    Activity
)

# Register your models here.
admin.site.register(Organisation)
admin.site.register(Site)
admin.site.register(Asset)
admin.site.register(Activity)