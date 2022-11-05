from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Document, Entity, Project


class IndexView(generic.ListView):
    template_name = "entity/index.html"
    context_object_name = "entities"

    def get_queryset(self):
        return Entity.objects.order_by("name")


def entityDetail(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    projects = Project.objects.filter(entity__id=entity_id)
    context = {"entity": entity, "projects": projects}
    return render(request, "entity/detail.html", context)


def projectDetail(request, entity_id, project_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    project = get_object_or_404(Project, pk=project_id)
    documents = Document.objects.filter(project_id=project_id)
    context = {"entity": entity, "project": project, "document": documents}
    return render(request, "project/detail.html", context)
