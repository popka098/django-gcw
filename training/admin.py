"""training admin"""
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

import training.models as models

# классы обработки данных
class Task_9_Resource(resources.ModelResource):
    """ресурс для загрузки бд слов задания 9

    """
    class Meta:
        """мета класс для Task_9

        """
        model = models.Task9
    
    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
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
    """ресурс для загрузки бд слов задания 10

    """
    class Meta:
        """мета класс для Task_10

        """
        model = models.Task10

    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
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
    """ресурс для загрузки бд слов задания 11

    """
    class Meta:
        """мета класс для Task_11

        """
        model = models.Task11

    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
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
    """ресурс для загрузки бд слов задания 12

    """
    class Meta:
        """мета класс для Task_12

        """
        model = models.Task12

    
    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
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
    """админка задания 9

    """
    resource_class = Task_9_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task_10_Admin(ImportExportActionModelAdmin):
    """админка задания 10

    """
    resource_class = Task_10_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task_11_Admin(ImportExportActionModelAdmin):
    """админка задания 11

    """
    resource_class = Task_11_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task_12_Admin(ImportExportActionModelAdmin):
    """админка задания 12

    """
    resource_class = Task_12_Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


# регистрация
admin.site.register(models.Task9, Task_9_Admin)
admin.site.register(models.Task10, Task_10_Admin)
admin.site.register(models.Task11, Task_11_Admin)
admin.site.register(models.Task12, Task_12_Admin)