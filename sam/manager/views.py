from django.views import generic, View
from django import forms
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from .models import Document, Entity, Project
from .files import store_file


class EntityListView(generic.ListView):
    context_object_name = "entities"
    model = Entity


class EntityDetailView(generic.DetailView):
    model = Entity


class AddDocumentForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        model = Document
        fields = ["project", "file"]


class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddDocumentForm(initial={"project": context["object"].id})
        return context


class AddDocumentFormView(SingleObjectMixin, FormView):
    model = Document
    form_class = AddDocumentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            file = store_file(request.FILES["file"])
            user_file_name = form.cleaned_data["file"].name
            self.object = Document.objects.create(
                name=user_file_name, stored_id=file[0], footprint=file[1], project=form.cleaned_data["project"]
            )

            return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("manager:project", kwargs={"pk": self.object.project.id})


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        view = ProjectDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AddDocumentFormView.as_view()
        return view(request, *args, **kwargs)
