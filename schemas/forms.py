from django import forms
from django.forms import inlineformset_factory

from schemas.models import Schema, Column


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ["name", "separator", "string_char"]


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ["name", "data_type", "order"]


ColumnFormSet = inlineformset_factory(
    Schema,
    Column,
    form=ColumnForm,
    extra=1,
    can_delete=False,
)