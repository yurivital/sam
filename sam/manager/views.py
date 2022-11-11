from django import forms
from django.urls import reverse
from django.views import View, generic
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, redirect

from .files import store_file
from .models import Document, Entity, Project


class EntityListView(generic.ListView):
    context_object_name = "entities"
    model = Entity


class EntityDetailView(generic.DetailView):
    model = Entity


class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddDocumentForm(initial={"project": context["object"].id})
        return context


class AddDocumentForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        model = Document
        fields = ["project", "file", "language"]


class AddDocumentFormView(SingleObjectMixin, FormView):
    model = Document
    form_class = AddDocumentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            file = store_file(request.FILES["file"])
            user_file_name = form.cleaned_data["file"].name
            self.object = Document.objects.create(
                name=user_file_name,
                stored_id=file["name"],
                footprint=file["footprint"],
                size=file["size"],
                project=form.cleaned_data["project"],
                language=form.cleaned_data["language"],
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


class ActionView(View):
    def get(self, request, *args, **kwargs):
        doc = get_object_or_404(Document, pk=kwargs["doc_id"])
        return redirect("manager:project", permanent=False, pk=doc.project.id)
