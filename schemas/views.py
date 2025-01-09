from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from schemas.mixins import SchemaWithColumnMixin
from schemas.models import Schema


class SchemaListView(ListView):
    model = Schema
    context_object_name = 'schemas'
    template_name = 'schemas/schema_list.html'


class SchemaCreateView(SchemaWithColumnMixin, CreateView):
    model = Schema
    success_url = reverse_lazy("schemas:schema_list")