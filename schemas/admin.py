from django.contrib import admin

from schemas.models import Schema, Column


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass