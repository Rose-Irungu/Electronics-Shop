from django.contrib import admin
from .models import ElectronicsData
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Resource class for import/export
class ElectronicsDataResource(resources.ModelResource):
    class Meta:
        model = ElectronicsData

# Register the model using ImportExportModelAdmin
@admin.register(ElectronicsData)
class ElectronicsAdmin(ImportExportModelAdmin):
    resource_class = ElectronicsDataResource
