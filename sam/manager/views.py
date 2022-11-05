from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Document, Entity, Project


class EntityListView(generic.ListView):
    context_object_name = "entities"
    model = Entity


class EntityDetailView(generic.DetailView):
    model = Entity


def projectDetail(request, entity_id, project_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    project = get_object_or_404(Project, pk=project_id)
    documents = Document.objects.filter(project_id=project_id)
    context = {"entity": entity, "project": project, "document": documents}
    return render(request, context)
