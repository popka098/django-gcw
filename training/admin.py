"""training admin"""
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from training import models

# Register your models here.


# классы обработки данных
class Task9Resource(resources.ModelResource):
    """ресурс для загрузки бд слов задания 9

    """
    class Meta:
        """мета класс для Task_9

        """
        model = models.Task9


    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
        word = row["Word"]
        passed = row["Pass"]
        print(word, passed)
        if (
            len(word) == 0 or
            len(passed) == 0 or
            len(word) != len(passed) or
            passed.count(".") != 1
        ):
            return True
        return False


class Task10Resource(resources.ModelResource):
    """ресурс для загрузки бд слов задания 10

    """
    class Meta:
        """мета класс для Task_10

        """
        model = models.Task10


    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
        word = row["Word"]
        passed = row["Pass"]
        print(word, passed)
        if (
            len(word) == 0 or
            len(passed) == 0 or
            len(word) != len(passed) or
            passed.count(".") != 1
        ):
            return True
        return False


class Task11Resource(resources.ModelResource):
    """ресурс для загрузки бд слов задания 11

    """
    class Meta:
        """мета класс для Task_11

        """
        model = models.Task11


    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
        word = row["Word"]
        passed = row["Pass"]
        print(word, passed)
        if (
            len(word) == 0 or
            len(passed) == 0 or
            len(word) != len(passed) or
            passed.count(".") != 1
        ):
            return True
        return False


class Task12Resource(resources.ModelResource):
    """ресурс для загрузки бд слов задания 12

    """
    class Meta:
        """мета класс для Task_12

        """
        model = models.Task12


    def skip_row(self, instance, original, row, import_validation_errors=None):
        """валидация слова

        """
        word = row["Word"]
        passed = row["Pass"]
        print(word, passed)
        if (
            len(word) == 0 or
            len(passed) == 0 or
            len(word) != len(passed) or
            passed.count(".") != 1
        ):
            return True
        return False


# Импорт данных на странице
class Task9Admin(ImportExportActionModelAdmin):
    """админка задания 9

    """
    resource_class = Task9Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task10Admin(ImportExportActionModelAdmin):
    """админка задания 10

    """
    resource_class = Task10Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task11Admin(ImportExportActionModelAdmin):
    """админка задания 11

    """
    resource_class = Task11Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


class Task12Admin(ImportExportActionModelAdmin):
    """админка задания 12

    """
    resource_class = Task12Resource
    list_display = ("Word", "Context_Before", "Pass", "Context_After")
    search_fields = ("Word", "Context_Before", "Pass", "Context_After")


# регистрация
admin.site.register(models.Task9, Task9Admin)
admin.site.register(models.Task10, Task10Admin)
admin.site.register(models.Task11, Task11Admin)
admin.site.register(models.Task12, Task12Admin)