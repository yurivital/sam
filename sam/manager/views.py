import os.path
from django import forms
from django.urls import reverse
from django.views import View, generic
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, redirect

from .files import create_storage, hash_file
from .models import Document, Entity, Project
from .actions import perfom_ocr


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
            user_file_name = form.cleaned_data["file"].name
            storage = create_storage(user_file_name)
            fullpath = storage["fullpath"]
            file = request.FILES["file"]
            with open(fullpath, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            self.object = Document.objects.create(
                name=user_file_name,
                stored_id=storage["storage_id"],
                footprint=hash_file(fullpath),
                size=os.path.getsize(fullpath),
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
        match kwargs["action"]:
            case "ocr":
                perfom_ocr(doc)

        return redirect("manager:project", permanent=False, pk=doc.project.id)
