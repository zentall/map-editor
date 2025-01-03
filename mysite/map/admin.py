from django.contrib import admin
from .models import *
from .forms import *


@admin.register(MapPage)
class MapPageAdmin(admin.ModelAdmin):
    form = MapPageAdminForm


@admin.register(MapSource)
class MapSourceAdmin(admin.ModelAdmin):
    form = MapSourceAdminForm


@admin.register(MapLayer)
class MapLayerAdmin(admin.ModelAdmin):
    form = MapLayerAdminForm
