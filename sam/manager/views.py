from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Document, Entity, Project


def index(request):
    entities = Entity.objects.order_by("name")
    context = {'entities': entities}
    return render(request, 'entity/index.html', context)


def entityDetail(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    projects = Project.objects.filter(entity__id=entity_id)
    context = {'entity': entity, 'projects': projects}
    return render(request, 'entity/detail.html', context)


def projectDetail(request, entity_id, project_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    project = get_object_or_404(Project, pk=project_id)
    documents = Document.objects.filter(project_id=project_id)
    context = {'entity': entity, 'project': project, 'document': documents}
    return render(request, 'project/detail.html', context)
