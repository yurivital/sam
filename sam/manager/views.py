from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Document, Entity, Project


class EntityListView(generic.ListView):
    context_object_name = "entities"
    model = Entity


class EntityDetailView(generic.DetailView):
    model = Entity


class ProjectDetailView(generic.DetailView):
    model = Project
