from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from bhot.transplants import forms, models, resources


@admin.register(models.Transplant)
class TransplantAdmin(ImportExportModelAdmin):
    resource_class = resources.TransplantResource


@admin.register(models.Biopsy)
class BiopsyAdmin(ImportExportModelAdmin):
    resource_class = resources.BiopsyResource


@admin.register(models.Histology)
class HistologyAdmin(ImportExportModelAdmin):
    resource_class = resources.HistologyResource


@admin.register(models.SequencingData)
class SequencingDataAdmin(ImportExportModelAdmin):
    resource_class = resources.SequencingDataResource
    readonly_fields = ("file_path",)


class FileUploadInline(admin.TabularInline):
    model = models.FileUpload
    max_num = 0


@admin.register(models.FileUploadBatch)
class FileUploadBatchAdmin(admin.ModelAdmin):
    form = forms.FileUploadBatchAdminForm
    inlines = [FileUploadInline]

    def save_related(self, request, form, formsets, change):
        # From https://web.archive.org/web/20220107040356/
        # https://xn--w5d.cc/2019/09/18/minimalistic-multiupload-in-django-admin.html
        # ModelAdmin handles saving the object separately and only
        # calls form’s save() method with commit=False.
        # We must call the save_files method manually.
        super().save_related(request, form, formsets, change)
        form.save_files(form.instance)