from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

import training.models as models

# классы обработки данных
class Task_9_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_9
class Task_10_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_10

class Task_11_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_11

class Task_12_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_12

class Task_15_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_15

# Ввод данных на странице
class Task_9_Admin(ImportExportActionModelAdmin):
    resource_class = Task_9_Resource

class Task_10_Admin(ImportExportActionModelAdmin):
    resource_class = Task_10_Resource

class Task_11_Admin(ImportExportActionModelAdmin):
    resource_class = Task_11_Resource

class Task_12_Admin(ImportExportActionModelAdmin):
    resource_class = Task_12_Resource

class Task_15_Admin(ImportExportActionModelAdmin):
    resource_class = Task_15_Resource


# регистрация
admin.site.register(models.Task_9, Task_9_Admin)
admin.site.register(models.Task_10, Task_10_Admin)
admin.site.register(models.Task_11, Task_11_Admin)
admin.site.register(models.Task_12, Task_12_Admin)
admin.site.register(models.Task_15, Task_15_Admin)