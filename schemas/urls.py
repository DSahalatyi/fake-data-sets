from django.urls import path

from schemas.views import SchemaListView, SchemaCreateView

app_name = "schemas"

urlpatterns = [
    path("", SchemaListView.as_view(), name="schema_list"),
    path("create/", SchemaCreateView.as_view(), name="schema_create"),
]