from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

import training.models as models

# классы обработки данных
class Task_9_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_9
    
    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        _Word = row["Word"]
        _Pass = row["Pass"]
        print(_Word, _Pass)
        if (
            len(_Word) == 0 or 
            len(_Pass) == 0 or 
            len(_Word) != len(_Pass) or
            _Pass.count(".") != 1
        ):
            return True
        return False
            

class Task_10_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_10

    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        _Word = row["Word"]
        _Pass = row["Pass"]
        print(_Word, _Pass)
        if (
            len(_Word) == 0 or 
            len(_Pass) == 0 or 
            len(_Word) != len(_Pass) or
            _Pass.count(".") != 1
        ):
            return True
        return False

class Task_11_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_11

    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        _Word = row["Word"]
        _Pass = row["Pass"]
        print(_Word, _Pass)
        if (
            len(_Word) == 0 or 
            len(_Pass) == 0 or 
            len(_Word) != len(_Pass) or
            _Pass.count(".") != 1
        ):
            return True
        return False


class Task_12_Resource(resources.ModelResource):
    class Meta:
        model = models.Task_12

    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        _Word = row["Word"]
        _Pass = row["Pass"]
        print(_Word, _Pass)
        if (
            len(_Word) == 0 or 
            len(_Pass) == 0 or 
            len(_Word) != len(_Pass) or
            _Pass.count(".") != 1
        ):
            return True
        return False


# Импорт данных на странице
class Task_9_Admin(ImportExportActionModelAdmin):
    resource_class = Task_9_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task_10_Admin(ImportExportActionModelAdmin):
    resource_class = Task_10_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task_11_Admin(ImportExportActionModelAdmin):
    resource_class = Task_11_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task_12_Admin(ImportExportActionModelAdmin):
    resource_class = Task_12_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


# регистрация
admin.site.register(models.Task_9, Task_9_Admin)
admin.site.register(models.Task_10, Task_10_Admin)
admin.site.register(models.Task_11, Task_11_Admin)
admin.site.register(models.Task_12, Task_12_Admin)