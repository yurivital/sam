from django.urls import path

from . import views

app_name = "manager"
urlpatterns = [
    path("", views.EntityListView.as_view(), name="index"),
    path("entity/<int:pk>/", views.EntityDetailView.as_view(), name="entity"),
    path(
        "entity/<int:entity_id>/project/<int:project_id>/",
        views.projectDetail,
        name="project",
    ),
]
