from django.shortcuts import redirect

from schemas.forms import SchemaForm, ColumnFormSet


class SchemaWithColumnMixin:
    form_class = SchemaForm
    template_name = "schemas/schema_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["column_formset"] = ColumnFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["column_formset"] = ColumnFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        column_formset = context["column_formset"]
        if form.is_valid() and column_formset.is_valid():
            schema = form.save(commit=False)
            schema.created_by = self.request.user
            schema.save()
            column_formset.instance = schema
            column_formset.save()
            return redirect("schemas:schema_list")
        else:
            return self.form_invalid(form)
